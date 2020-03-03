from Calculator.Calculator import Calculator
from StatisticsFunctions.Mean import mean
from StatisticsFunctions.Median import median
from StatisticsFunctions.Mode import mode

class Statistics(Calculator):
    def mean(self, data):
        self.result = mean(data)
        return self.result
    def median(self, data):
        self.result = median(data)
        return self.result
    def mode(self, data):
        self.result = mode(data)
        return self.result