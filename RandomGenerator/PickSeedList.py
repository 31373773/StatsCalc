from numpy.random import seed
from RandomGenerator.ItemInList import ItemInList

class PickSeedList():
    @staticmethod
    def pickSeed(Seed, lst):
        seed(Seed)
        newLst = ItemInList.pickItem(lst)
        return newLst