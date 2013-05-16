# -*- coding: utf-8 -*-
import unittest
import text


class TestPreProcessor(unittest.TestCase):

    def setUp(self):
        self.input_text = unicode("""La Piedad del Vaticano es un grupo escultórico en mármol realizado por Miguel Ángel entre 1498 y 1499. Sus dimensiones son 174 por 195 cm. Se encuentra en la Basílica de San Pedro del Vaticano.""", encoding='utf8')
        self.input_sentences = [
            unicode('La Piedad del Vaticano es un grupo escultórico en mármol realizado por Miguel Ángel entre 1498 y 1499.', encoding='utf-8'),
            unicode('Sus dimensiones son 174 por 195 cm.', encoding='utf-8'),
            unicode('Se encuentra en la Basílica de San Pedro del Vaticano .', encoding='utf-8'),
        ]

    def test_tokenize(self):
        sentences = self.input_sentences
        expect =[
            unicode('La Piedad del Vaticano es un grupo escultórico en mármol realizado por Miguel Ángel entre 1498 y 1499 .', encoding='utf-8'),
            unicode('Sus dimensiones son 174 por 195 cm .', encoding='utf-8'),
            unicode('Se encuentra en la Basílica de San Pedro del Vaticano .', encoding='utf-8'),
        ] 
        actual = text.tokenize('es', sentences)
        self.assertEqual(expect, actual)

    def test_prepare(self):
        input_text = self.input_text
        expect = '\n'.join(
            [
                unicode('la piedad del vaticano es un grupo escultórico en mármol realizado por miguel ángel entre 1498 y 1499 .', encoding='utf-8'),
                unicode('sus dimensiones son 174 por 195 cm .', encoding='utf-8'),
                unicode('se encuentra en la basílica de san pedro del vaticano .', encoding='utf-8'),
            ]
        )
        actual = text.PreProcessor('spanish').prepare(input_text)
        self.assertEqual(expect, actual)
