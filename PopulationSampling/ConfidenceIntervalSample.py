from PopulationSampling.ConfidenceIntervalPop import ConfidenceIntervalPop
from PopulationSampling.RandomSampling import SimpleSampling


class ConfidenceInterval(ConfidenceIntervalPop):
    @staticmethod
    def confidenceInterval(conf, data, sd, higher):
        sample = SimpleSampling.generateSampling(sd, data, higher)
        return ConfidenceIntervalPop.confidenceIntervalPop(conf, sample)