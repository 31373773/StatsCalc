import unittest
from StatisticsFunctions.Mean import Mean
from StatisticsFunctions.Median import Median
from StatisticsFunctions.Mode import Mode
from StatisticsFunctions.Variance import Variance
from StatisticsFunctions.StandardDeviation import StandardDeviation
from StatisticsFunctions.MeanDeviation import MeanDeviation
from StatisticsFunctions.Quartiles import Quartiles
from StatisticsFunctions.Covariance import Covariance
from StatisticsFunctions.Skewness import Skewness
from StatisticsFunctions.PopulationCorrelation import PopulationCorrelation
from StatisticsFunctions.SampleCorrelation import SampleCorrelation
from StatisticsFunctions.ZScore import zScore

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [1, 2, 3, 4]
        self.testData2 = [1, 2, 2, 3, 4]
        self.testData3 = [1, 2, 4, 5]

    def test_StatisticFunctions_Mean(self):
        self.assertEqual(2.5, Mean.mean(self.testData))

    def test_StatisticFunctions_Median(self):
        self.assertEqual(2.5, Median.median(self.testData))

    def test_StatisticFunctions_Mode(self):
        self.assertEqual(2, Mode.mode(self.testData2))

    def test_StatisticFunctions_Variance(self):
        self.assertEqual(1.25, Variance.variance(self.testData))

    def test_StatisticFunctions_StandardDeviation(self):
        self.assertEqual(1.118033988749895, StandardDeviation.standardDeviation(self.testData))

    def test_StatisticFunctions_Quartiles(self):
        self.assertEqual([1.75, 2.5, 3.25], Quartiles.quartiles(self.testData))

    def test_StatisticFunctions_Covariance(self):
        self.assertEqual(2.333333333333333, Covariance.covariance(self.testData, self.testData3))

    def test_StatisticFunctions_Skewness(self):
        self.assertEqual(0, Skewness.skewness(self.testData))

    def test_StatisticFunctions_MeanDeviation(self):
        self.assertEqual(1, MeanDeviation.meanDeviation(self.testData))

    def test_StatisticFunctions_PopulationCorrelation(self):
        self.assertEqual(1.3199326582148883, PopulationCorrelation.popCor(self.testData, self.testData3))

    def test_StatisticFunctions_SampleCorrelation(self):
        self.assertEqual(1.084333414387259, SampleCorrelation.correlation(3, self.testData, self.testData3))

    def test_StatisticFunctions_ZScore(self):
        self.assertEqual(0.4472135954999579, zScore.zscore(4, self.testData))

