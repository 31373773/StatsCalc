from Calculator.Calculator import Calculator
from PopulationSampling import RandomSampling
from StatisticsFunctions.Mean import Mean
from StatisticsFunctions.Median import Median
from StatisticsFunctions.Mode import Mode
from StatisticsFunctions.PopulationCorrelation import PopulationCorrelation
from StatisticsFunctions.Quartiles import Quartiles
from StatisticsFunctions.Skewness import Skewness
from StatisticsFunctions.Variance import Variance
from StatisticsFunctions.StandardDeviation import StandardDeviation
from StatisticsFunctions.MeanDeviation import MeanDeviation
from RandomGenerator.RandNoSeed import RandomNoSeed
from RandomGenerator.RandwSeed import RandomWithSeed
from RandomGenerator.RandList import RandomList
from PopulationSampling.RandomSampling import SimpleSampling
from PopulationSampling.SystematicSampling import SystematicSampling
from PopulationSampling.ConfidenceIntervalSample import ConfidenceInterval
from PopulationSampling.MarginError import MarginError
from PopulationSampling.Cochran import Cochran


class Statistics(Calculator):

    def mean(self, data):
        self.result = Mean(data)
        return self.result

    def median(self, data):
        self.result = Median.median(data)
        return self.result

    def mode(self, data):
        self.result = Mode.mode(data)
        return self.result

    def var(self, data):
        self.result = Variance.variance(data)
        return self.result

    def stdDev(self, data):
        self.result = StandardDeviation.standardDeviation(data)
        return self.result

    def meandeviation(self, data):
        self.result = MeanDeviation.meanDeviation(data)
        return self.result

    def quart(self, data):
        self.result = Quartiles.quartiles(data)
        return self.result

    def skew(self, data):
        self.result = Skewness.skewness(data)
        return self.result

    def popCo(self, data, data2):
        self.result = PopulationCorrelation.popCor(data, data2)
        return self.result

    def randomNoSeedInt(self, a, b):
        self.result = RandomNoSeed.randomInt(a, b)
        return self.result

    def randomNoSeedDec(self, a, b):
        self.result = RandomNoSeed.randomFloat(a, b)
        return self.result

    def randomWithSeedInt(self, sd, a, b):
        self.result = RandomWithSeed.randomInt(sd, a, b)
        return self.result

    def randomWithSeedDec(self, sd, a, b):
        self.result = RandomWithSeed.randomFloat(sd, a, b)
        return self.result

    def randomListInt(self, a, b, lngth, sd):
        self.result = RandomList.lstInts(a, b, lngth, sd)
        return self.result

    def randomListDec(self, a, b, lngth, sd):
        self.result = RandomList.lstFloats(a, b, lngth, sd)
        return self.result


    def SystematicSampling(self, lst, n, k):
        self.result = SystematicSampling.systematicSampling(lst, n, k)
        return self.result


    def MarginError(self, data, n):
        self.result = MarginError.marginError(data, n)
        return self.result

    def test_Cochran(self, sd, data, rnge):
        self.result = Cochran.cochran(sd, data, rnge)
        return self.result

