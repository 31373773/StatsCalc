from numpy.random import seed
from numpy.random import uniform
from numpy.random import randint

class RandomWithSeed():
    @staticmethod
    def randomFloat(Seed, a, b):
        seed(Seed)
        num = uniform(a, b)
        return num

    @staticmethod
    def randomInt(Seed, a, b):
        seed(Seed)
        num = randint(a, b)
        if isinstance(a, float):
            return RandomWithSeed.randomFloat(Seed, a, b)
        return num

