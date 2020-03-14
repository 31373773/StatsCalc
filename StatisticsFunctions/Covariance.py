import numpy


class Covariance():
    @staticmethod

    def covariance(a, b):

        return numpy.cov(a, b)[0, 1]