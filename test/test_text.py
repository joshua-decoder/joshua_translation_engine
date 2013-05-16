# -*- coding: utf-8 -*-
import unittest
import text


class TestPreProcessor(unittest.TestCase):

    def test_splitter_es_en(self):
        input_text = unicode("""La Piedad del Vaticano es un grupo escultórico en mármol realizado por Miguel Ángel entre 1498 y 1499. Sus dimensiones son 174 por 195 cm. Se encuentra en la Basílica de San Pedro del Vaticano.""", encoding='utf8')
        #input_text = u"""La Piedad del Vaticano es un grupo escultórico en mármol realizado por Miguel Ángel entre 1498 y 1499. Sus dimensiones son 174 por 195 cm. Se encuentra en la Basílica de San Pedro del Vaticano."""

        expect = [
            unicode('la piedad del vaticano es un grupo escultórico en mármol realizado por miguel ángel entre 1498 y 1499.', encoding='utf-8'),
            unicode('sus dimensiones son 174 por 195 cm.', encoding='utf-8'),
            unicode('se encuentra en la basílica de san pedro del vaticano.', encoding='utf-8'),
            ]
        actual = text.PreProcessor('spanish').prepare(input_text)
        self.assertEqual(expect, actual)


class TestDecoder(unittest.TestCase):

    def test_splitter_es_en(self):
        pass
