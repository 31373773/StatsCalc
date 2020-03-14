from RandomGenerator.SelectwSeed import SelectWithSeed

from numpy.random import seed


class SimpleSampling(SelectWithSeed):
    @staticmethod

    def generateSampling(sd, lst, rnge):
        seed(sd)
        return SelectWithSeed(sd, lst, rnge)