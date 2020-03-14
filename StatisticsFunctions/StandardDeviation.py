from MathOperations.root import Root
from StatisticsFunctions.Variance import Variance

class StandardDeviation:
   @staticmethod
   def standardDeviation(data):
      return Root.root(Variance.variance(data), 2)