from piglatin import PigLatin

class PigLatinTranslator:
    def __init__(self):
        self.translator = None

    def PigLatinTranslator(self, phrase: str):
        self.translator = PigLatin(phrase)
        return self.translator

    def translate(self) -> str:
        return self.translator.translate()

    def get_phrase(self) -> str:
        return self.translator.get_phrase()

    def translate(self) -> str:
        return self.translator.translate()
