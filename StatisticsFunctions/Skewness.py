from StatisticFunctions.StandardDeviation import StandardDeviation
from scipy import stats
import numpy

class PopulationCorrelation():
    @staticmethod

    def popCorrelation(a, b):
        cov = Covariance.covariance(a, b)
        a = StandardDeviation.standardDeviation(a)
        b = StandardDeviation.standardDeviation(b)
        return cov/(stdDevA*stdDevB)