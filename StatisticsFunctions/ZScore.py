from Statistics.Mean import mean
from StatisticsFunctions.StandardDeviation import StandardDeviation
from MathOperations import division
from RandomGenerator.RandwSeed import RandomWithSeed

class zScore():
    def zScore(data):
        x = RandomWithSeed(data)
        meanData = mean(data)
        sd = StandardDeviation(data)
        numerator = x - meanData
        z = division(numerator, sd)
        return z