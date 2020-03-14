from PopulationSampling.MarginError import MarginError
from StatisticsFunctions.StandardDeviation import StandardDeviation
from MathOperations.exponentiation import Exponentiation

class SampleSizeKnownPop():
    @staticmethod

    def sampleSize(sd, data):

        e = MarginError.marginError(sd, data)
        stdDev = StandardDeviation.StandardDeviation(data)
        val = (1.96 * stdDev) / e
        sample = Exponentiation.sqr(val, 2)

        return sample