import unittest
from random import randint, seed

from PopulationSampling.Cochran import Cochran
from PopulationSampling.RandomSampling import SimpleSampling
from PopulationSampling.MarginError import MarginError
from PopulationSampling.SampleSizeKnownPop import SampleSizeKnownPop
from PopulationSampling.SampleSizeUnknownPop import SampleSizeUnkownPop

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        seed(4)
        self.testData = randint(0, 50)

    def test_generate_sample(self):
        result = SimpleSampling.generateSampling(3, self.testData, 5)
        self.assertEqual(result, [3, 1, 2, 1, 1])


    def test_Margin_Error(self):
        result = MarginError.marginError(self.testData, 3)
        self.assertEqual(result, -14.133333333333335)

    def test_Cochran(self):
        result = Cochran.cochran(3, self.testData, 4)
        self.assertEqual(result, 0.0010094984628091588)

    def test_SampleSizeUnKnownPop(self):
        result = SampleSizeUnkownPop.sampleSize(3, self.testData, .5)
        self.assertEqual(result, 0.0010094984628091588)

    def test_SampleSizeKnownPop(self):
        result = SampleSizeKnownPop.sampleSize(3, self.testData)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()