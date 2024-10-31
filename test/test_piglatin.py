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


