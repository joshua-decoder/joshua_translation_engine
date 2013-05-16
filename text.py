import nltk


class PreProcessor(object):
    """
    Prepares raw text for input to a Joshua decoder
    """
    def __init__(self, lang):
        self._tokenize = nltk.data.load('tokenizers/punkt/%s.pickle' % lang).tokenize

    def prepare(self, text):
        return [sent.lower() for sent in self._tokenize(text)]

class TestBundleConfig(object):

    def test_loaded_config(self):
        """
        should be able to know the source and target lang after reading a
        config file from a bundle.
        """
