from random import sample
from random import shuffle

class RandomSampling():
    def RandomSampling(p, num):
        shuffle(p)
        return sample(p, num)