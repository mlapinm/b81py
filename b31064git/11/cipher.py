from itertools import cycle
class Cipher:
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    @classmethod
    def get_char(cls, n):
        return cls.alpha[n % 26]

class Caesar(Cipher):
    @classmethod
    def encode(cls, text, n=5):
        res = [Cipher.get_char(cls.alpha.index(c) + n) if c in cls.alpha else c for c in text]
        return ''.join(res)

    @classmethod
    def decode(cls, text, n=5):
        return cls.encode(text, -n)


class Rot13:
    @classmethod
    def encode(cls, text):
        return Caesar.encode(text, 13)

    @classmethod
    def decode(cls, text):
        return cls.encode(text)

class Vigenere(Cipher):
    @classmethod
    def __process(cls, text, key, fn):
        result = [
            Cipher.get_char(fn(Cipher.alpha.index(a), Cipher.alpha.index(b)))
            if a in Cipher.alpha else a 
            for a,b in zip(text, cycle(key))
        ]
        return ''.join(result)

    @classmethod
    def decode(cls, text, key):
        return cls.__process(text, key, lambda x, y: x - y)

    @classmethod
    def encode(cls, text, key):
        return cls.__process(text, key, lambda x, y: x + y)

