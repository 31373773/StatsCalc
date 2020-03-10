from numpy.random import randint

class ItemInList():
    @staticmethod
    def pickItem(lst):
        return lst[randint(0, len(lst)-1)]