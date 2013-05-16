import os
from subprocess import Popen, PIPE
import sys
import nltk
import env

env.assert_valid_env()


def _penn_treebank_tokenize(lang_short_code, text):
    runner_path = os.path.join(
        os.environ['JOSHUA'],
        'scripts',
        'training',
        'penn-treebank-tokenizer.perl'
    )
    options = ['-l', lang_short_code]
    p = Popen(
        [runner_path] + options,
        stdin=PIPE,
        stderr=PIPE,
        stdout=PIPE,
        env=os.environ
    )
    out, err = p.communicate(text.encode('utf8'))
    sys.stderr.write(err.encode('utf8') + '\n')
    return unicode(out.strip(), encoding='utf8').split('\n')

def tokenize(lang_short_code, sentences):
    """
    Returns a string with tokenized parts separated by a space character
    """
    if lang_short_code not in ['en', 'es']:
        lang_short_code = 'en'

    text = '\n'.join(sentences)

    return _penn_treebank_tokenize(lang_short_code, text)

def detokenize(sentence):
    """
    Returns a string with tokenized parts separated by a space character
    """
    pass


class PreProcessor(object):
    """
    Prepares raw text for input to a Joshua Decoder:
    1. Sentence-splitting
    2. tokenization
    3. lowercasing
    4. joining sentences with '\n'
    """
    def __init__(self, lang_long_name):
        self._lang = lang_long_name
        self._sentence_splitter = nltk.data.load(
            'tokenizers/punkt/%s.pickle' % lang_long_name
        ).tokenize

    def prepare(self, text):
        sentences = self._sentence_splitter(text)
        tokenized_sentences = tokenize(self._lang, sentences)
        lc_tokenized_sentences = [sent.lower() for sent in tokenized_sentences]
        return '\n'.join(lc_tokenized_sentences)


class PostProcessor(object):
    """
    Prepares text returned by the Joshua decoder for response to client
    """
    def __init__(self, lang):
        pass
