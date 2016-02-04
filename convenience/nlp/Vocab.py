from pandas import DataFrame, Series, concat

class Vocab(object):
    def __init__(self):
        self.vocab = DataFrame()
        self.w2i = Series() # word to index Series
        self.i2w = Series() # index to word Series
        self.size = 0       # vocab size

