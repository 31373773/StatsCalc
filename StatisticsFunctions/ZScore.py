from Statistics.Mean import mean
from StatisticsFunctions.StandardDeviation import StandardDeviation
from MathOperations import division

import random
class zScore():
    def zScore(data):
        x = random.choice(data)
        meanData = mean(data)
        sd = StandardDeviation(data)
        numerator = x - meanData
        z = division(numerator, sd)
        return z