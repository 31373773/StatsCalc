from numpy.random import seed
from numpy.random import randint
from numpy.random import uniform

class RandomList():
    @staticmethod
    def lstFloats(x, y, length, Seed):
        lst = []
        seed(Seed)

        for var in range(length):
            num = uniform(x, y)
            lst.append(num)
        return lst

    @staticmethod
    def lstInts(x, y, length, Seed):
        if isinstance(x, float):
            return lstInts(x, y, length, Seed)
        lst = []
        seed(Seed)

        for var in range(length):
            num = randint(x, y)
            lst.append(num)

        return lst