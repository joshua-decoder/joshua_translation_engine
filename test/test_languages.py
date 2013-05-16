import unittest
import languages


class TestLanguageAliasesObj(unittest.TestCase):

    def test_new_lang_from_short_name_valid(self):
        self.assertIsInstance(
            languages.new_lang_from_short_name('en'),
            languages.LanguageAliases
        )

    def test_new_lang_from_short_name_valid_short(self):
        self.assertEqual(
            'en',
            languages.new_lang_from_short_name('en').short_name,
        )

    def test_new_lang_from_short_name_valid_long(self):
        self.assertEqual(
            'english',
            languages.new_lang_from_short_name('en').long_english_name,
        )

    def test_new_lang_from_long_name_valid_long(self):
        self.assertEqual(
            'english',
            languages.new_lang_from_long_english_name('english').long_english_name,
        )

    def test_new_lang_from_long_name_valid_short(self):
        self.assertEqual(
            'es',
            languages.new_lang_from_long_english_name('spanish').short_name,
        )
        self.assertEqual(
            'es',
            languages.new_lang_from_long_english_name('Spanish').short_name,
        )

    def test_new_lang_from_short_name_invalid(self):
        self.assertRaises(
            KeyError,
            languages.new_lang_from_short_name,
            'kl',
        )

    def test_new_lang_from_long_name_invalid(self):
        self.assertRaises(
            KeyError,
            languages.new_lang_from_long_english_name,
            'klingon',
        )
