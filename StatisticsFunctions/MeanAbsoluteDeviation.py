from StatisticFunctions.Mean import Mean
from numpy import absolute

class MeanDeviation:
    @staticmethod
    def meanDeviation(data):
        m = Mean.mean(data)
        total = 0
        l = len(data)
        for i in data:
            total = total + absolute(i-m)
        return (total/l)