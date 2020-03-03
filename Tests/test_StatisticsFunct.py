import unittest
from StatisticsFunctions.Mean import mean
from StatisticsFunctions.Median import median
from StatisticsFunctions.Mode import mode
from Statistics.RandomData import getRandomNums

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = getRandomNums(1, 1, 100, 20)

    def test_StatisticFunctions_Mean(self):
        self.assertEqual(38.95, mean(self.testData))

    def test_StatisticFunctions_Median(self):
        self.assertEqual(27.5, median(self.testData))

    def test_StatisticFunctions_Mode(self):
        self.assertEqual(2, mode(self.testData))