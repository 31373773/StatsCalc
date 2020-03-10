from numpy.random import randint
from numpy.random import uniform


class RandomNoSeed():
    @staticmethod
    def randomFloat(a, b):
        return uniform(a, b)

    @staticmethod
    def randomInt(a, b):
        if isinstance(a, float):
            return RandomNoSeed.randomFloat(a, b)
        return randint(a, b)

