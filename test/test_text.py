# -*- coding: utf-8 -*-
import unittest
import text
import mock


class TestPreProcessor(unittest.TestCase):

    def setUp(self):
        self.input_text = unicode(
            'La Piedad del Vaticano es un grupo escultórico en mármol '
            'realizado por Miguel Ángel entre 1498 y 1499. Sus dimensiones '
            'son 174 por 195 cm. Se encuentra en la Basílica de San Pedro del '
            'Vaticano.', encoding='utf8')

        self.input_sentences = [
            unicode(
                'La Piedad del Vaticano es un grupo escultórico en mármol '
                'realizado por Miguel Ángel entre 1498 y 1499.',
                encoding='utf-8'),
            unicode(
                'Sus dimensiones son 174 por 195 cm.', encoding='utf-8'),
            unicode(
                'Se encuentra en la Basílica de San Pedro del Vaticano .',
                encoding='utf-8'),
        ]

    def test_tokenize(self):
        sentences = self.input_sentences
        expect = [
            unicode(
                'La Piedad del Vaticano es un grupo escultórico en mármol '
                'realizado por Miguel Ángel entre 1498 y 1499 .',
                encoding='utf-8'),
            unicode(
                'Sus dimensiones son 174 por 195 cm .',
                encoding='utf-8'),
            unicode(
                'Se encuentra en la Basílica de San Pedro del Vaticano .',
                encoding='utf-8'),
        ]
        actual = text.tokenize('es', sentences)
        self.assertEqual(expect, actual)

    def test_prepare(self):
        input_text = self.input_text
        expect = '\n'.join(
            [
                unicode(
                    'la piedad del vaticano es un grupo escultórico en mármol '
                    'realizado por miguel ángel entre 1498 y 1499 .',
                    encoding='utf-8'),
                unicode(
                    'sus dimensiones son 174 por 195 cm .',
                    encoding='utf-8'),
                unicode(
                    'se encuentra en la basílica de san pedro del vaticano .',
                    encoding='utf-8'),
            ]
        )
        lang_aliases = mock.Mock(long_english_name='spanish', short_name='es')
        actual = text.PreProcessor(lang_aliases).prepare(input_text)
        self.assertEqual(expect, actual)


haiku = """From time to time
The clouds give rest
To the moon-beholders.

- Bashō""".decode('utf8')

lorem = unicode(
    'Lorem ipsúm dolor sit amet, ut aliqua. '
    'Ut enim ad minim veniam, exercitation ullamco consequat.'
    '\n\n'
    'Duis aute irure dolor in fugiat nulla pariatur. '
    'Excepteur sint occaecat, mollit anim id est laborum.',
    encoding='utf8'
)

lorem_tok = """Lorem ipsúm dolor sit amet , ut aliqua .
Ut enim ad minim veniam , exercitation ullamco consequat .

Duis aute irure dolor in fugiat nulla pariatur .
Excepteur sint occaecat , mollit anim id est laborum .""".decode('utf8')

lorem_tok_lc = """lorem ipsúm dolor sit amet , ut aliqua .
ut enim ad minim veniam , exercitation ullamco consequat .

duis aute irure dolor in fugiat nulla pariatur .
excepteur sint occaecat , mollit anim id est laborum .""".decode('utf8')


class TestPostProcessor(unittest.TestCase):

    def test_merge_sentences(self):
        translation = haiku
        expect = (
            'From time to time The clouds give rest To the moon-beholders.'
            '\n\n- Bashō'.decode('utf8')
        )
        actual = text.merge_lines(translation)
        self.assertEqual(expect, actual)

    def test_prepare(self):
        lang_aliases = mock.Mock(long_english_name='spanish', short_name='es')

        expect = lorem
        actual = text.PostProcessor(lang_aliases).prepare(lorem_tok_lc)

        self.assertEqual(expect, actual)
