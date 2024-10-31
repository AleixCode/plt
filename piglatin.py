from gettext import translation

from pyparsing import Empty

def isVowel(char):
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return True
    return False


class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        translation = ""
        for word in [self.phrase]:
            value = ""
            firstLetter = word[0].lower()
            if isVowel(firstLetter):
                lastLetter = word[-1]
                if lastLetter == "y":
                    value = word + "nay"
                elif isVowel(lastLetter):
                    value = word + "yay"
                else:
                    value = word + "ay"
            else:
                value = word[1:] + word[0] + "ay"
            translation = translation +""+ value
        return translation