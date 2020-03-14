from StatisticsFunctions.Mean import Mean
from StatisticsFunctions.StandardDeviation import StandardDeviation
from RandomGenerator.PickSeedList import PickSeedList
from MathOperations.division import Division


class Zscore():
    @staticmethod

    def zscore(sd, data):
        X = PickSeedList.pickSeed(sd, data)
        meanData = Mean.Mean(data)
        sd = StandardDeviation.standardDeviation(data)
        z = Division.divide(X-meanData, sd)
        return z