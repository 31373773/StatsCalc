from StatisticsFunctions.ZScore import zScore
from PopulationSampling.MarginError import MarginError
from MathOperations.exponentiation import Exponentiation

class SampleSizeUnkownPop():
    @staticmethod

    def sampleSize(sd, data, percentage):
        z = zScore.zScore(sd)
        e = MarginError.marginError(sd, data)
        p = percentage
        q = 1 - p
        val = z/e
        sample = Exponentiation.sqr(val, 2) * p * q

        return sample