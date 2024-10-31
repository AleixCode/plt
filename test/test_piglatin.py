import unittest
from piglatin import PigLatin
from piglatintranslator import PigLatinTranslator
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def setUp(self):
        self.PigLatinTranslator = PigLatinTranslator()


    def test_get_phrase(self):
        self.PigLatinTranslator.PigLatinTranslator("hello world")
        self.assertEqual("hello world", self.PigLatinTranslator.get_phrase())

    def test_translate_empty_phrase(self):
        self.PigLatinTranslator.PigLatinTranslator("")
        self.assertEqual("nil", self.PigLatinTranslator.translate())

    def test_translate_signle_word_with_starting_vowel_ends_y(self):
        self.PigLatinTranslator.PigLatinTranslator("aly")
        self.assertEqual("alynay", self.PigLatinTranslator.translate())

    def test_translate_signle_word_with_starting_vowel_ends_vowel(self):
        self.PigLatinTranslator.PigLatinTranslator("ala")
        self.assertEqual("alayay", self.PigLatinTranslator.translate())

    def test_translate_signle_word_with_starting_vowel_ends_consonant(self):
        self.PigLatinTranslator.PigLatinTranslator("alz")
        self.assertEqual("alzay", self.PigLatinTranslator.translate())


