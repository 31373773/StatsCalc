import unittest
from RandomGenerator.RandNoSeed import RandomNoSeed
from RandomGenerator.RandwSeed import RandomWithSeed
from RandomGenerator.RandList import RandomList
from RandomGenerator.PickSeedList import PickSeedList
from RandomGenerator.SelectNoSeed import SelectWithoutSeed
from RandomGenerator.SelectwSeed import SelectWithSeed

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_RandomNoSeed_Int(self):
        result = RandomNoSeed.randomInt(0, 10)
        self.assertEqual(isinstance(result, int), True)

    def test_RandomNoSeed_Dec(self):
        result = RandomNoSeed.randomFloat(0, 10)
        self.assertEqual(isinstance(result, float), True)

    def test_RandomSeed_Int(self):
        result = RandomWithSeed.randomInt(4, 0, 10)
        result2 = RandomWithSeed.randomInt(4, 0, 10)
        self.assertEqual(result, result2)

    def test_RandomSeed_Dec(self):
        result = RandomWithSeed.randomFloat(4, 0, 10)
        result2 = RandomWithSeed.randomFloat(4, 0, 10)
        self.assertEqual(result, result2)

    def test_RandomListInt(self):
        result = RandomList.lstInts(0, 10, 5, 4)
        self.assertEqual(result, [7, 5, 1, 8, 7])

    def test_RandomListDec(self):
        result = RandomList.lstFloats(0, 10, 5, 4)
        self.assertEqual(result, [9.670298390136766, 5.4723224917572235,
                                  9.726843599648843, 7.148159936743647,
                                  6.977288245972709])

    def test_PickRandomNumber(self):
        lst = RandomList.lstInts(0, 10, 5, 4)
        result = PickSeedList.pickSeed(lst)
        self.assertEqual(result, 7)

    def test_PickSeedList(self):
        lst = RandomList.lstInts(0, 10, 5, 4)
        result = PickSeedList.pickSeed(3, lst)
        result2 = PickSeedList.pickSeed(3, lst)
        self.assertEqual(result, result2)

    def test_PickFromListNoSeed(self):
        lst = RandomList.lstInts(0, 10, 10, 3)
        result = SelectWithoutSeed.pickItem(lst, 5)
        self.assertEqual(result, [0, 3, 5, 8, 8])

    def test_PickFromListSeed(self):
        lst = RandomList.lstInts(0, 10, 10, 3)
        result = SelectWithSeed.pickItem(3, lst, 5)
        self.assertEqual(result, [9, 8, 9, 9, 8])