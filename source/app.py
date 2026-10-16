import random
import string
from abc import ABC, abstractmethod
import nltk



class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        """this class override this method to generate password."""
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int= 5):
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
    def __init__(self, number_of_words: int = 5, separator: str = "-", caplitalization: bool = False, vocabulary: list = None):
        
        if vocabulary is None:
            try:
                self.vocabulary = nltk.corpus.words.words() # this code about vocabulary list you want
            except LookupError:
                nltk.download("words", quiet=True)
                self.vocabulary = nltk.corpus.words.words()
        else:
            self.vocabulary = vocabulary

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


def pin_password_test():
    pin = PinGenerator()
    pin_pass = pin.generate()
    print(pin_pass)
    assert len(pin_pass) == 5


def random_password_test():
    rand = RandomPasswordGenerator(length=10, include_number=True, include_symbols=True)
    random_pass = rand.generate()
    print(random_pass)
    assert len(random_pass) == 10



def memorable_password_test():
    memorable = MemorablePasswordGenerator(number_of_words=5, separator="-", caplitalization=True, vocabulary=nltk.corpus.words.words())
    memorable_pass = memorable.generate()
    print(memorable_pass)
    assert len(memorable_pass.split("-")) == 5


def main():
    print("Testing PinGenerator:")
    pin_password_test()
    print("Testing RandomPassword:")
    random_password_test()
    print("Testing MemorablePassword:")
    memorable_password_test()


if __name__ == "__main__":
    main()