import random
import string
from abc import ABC, abstractmethod
import nltk

nltk.download("words", quiet=True)


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        """this class override this method to generate password."""
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length

    def generate(self) -> str:
        """Return a random numeric PIN of length `self.length`."""
        return "".join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    """
    this class generate random password.
    
    """
    def __init__(self, length: int = 8, include_number: bool = False, include_symbols: bool = False):
        self.length = length
        self.character = string.ascii_letters
        if include_number:
            self.character += string.digits
        if include_symbols:
            self.character += string.punctuation


    def generate(self) -> str:
        return "".join([random.choice(self.character) for _ in range(self.length)])

    
class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, number_of_words: int = 4, separator: str = "-", caplitalization: bool = False, vocabulary: list = None):
        
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words() # this code about vocabulary list you want

        self.number_of_words = number_of_words
        self.caplitalization = caplitalization
        self.separator = separator
        
    def generate(self):
        """
        generate password from list of vocabulary words(nltk).
        """

        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.caplitalization:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]

        return self.separator.join(password_words)


if __name__ == "__main__":
    pass_w = RandomPasswordGenerator()
    pass_m = MemorablePasswordGenerator()
    print(pass_w.generate())
    print(pass_m.generate())