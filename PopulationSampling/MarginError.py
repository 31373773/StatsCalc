from StatisticsFunctions.StandardDeviation import StandardDeviation
from StatisticsFunctions.ZScore import zScore
from MathOperations import root

class MarginError():
    @staticmethod
    def marginError(data, n):
        zscore = zScore(data)
        standardDeviation = StandardDeviation.StandardDeviation(data)
        MoE = zscore * (standardDeviation/(root(n, 2)))
        return MoE