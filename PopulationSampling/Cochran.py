from StatisticsFunctions.ZScore import zScore
from PopulationSampling.MarginError import MarginError
from PopulationSampling.PopulationProportion import PopulationProportion
from MathOperations.exponentiation import Exponentiation


class Cochran():
    @staticmethod
    def cochran(sd, data, rnge):
        z = zScore.zScore(data)
        p = PopulationProportion.proportion(sd, data, rnge)
        e = MarginError.marginError(sd, data)
        q = 1 - p

        cochran = (Exponentiation.sqr(z, 2) * p * q) / Exponentiation.sqr(e, 2)

        return cochran
