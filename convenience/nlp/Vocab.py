from pandas import DataFrame, Series, concat

################################################################################
#                                                                          VOCAB
################################################################################
class Vocab(object):
    """
    Vocabulary object, that stores frequency counts of words from some corpus,
    along with methods for trimming down the vocabulary size based on max
    number of items, and min frequency count.

    Allows you to convert from token strings to word indices, and vice versa.
    """
    ############################################################################
    # ==========================================================================
    #                                                                   __INIT__
    # ==========================================================================
    def __init__(self):
        self.vocab = DataFrame()
        self.w2i = Series() # word to index Series
        self.i2w = Series() # index to word Series
        self.size = 0       # vocab size

    # ==========================================================================
    #                                                                 WORD2INDEX
    # ==========================================================================
    def word2index(self, words):
        """
        Takes a word, or list of word, and returns their indices.

        :param words: (str, or list of strs)
        :return: (list of ints)
        """
        return list(self.w2i[words].fillna(0, inplace=False).astype(int))
    #                                                       FROM_TOKENIZED_LISTS
    # ==========================================================================
    def from_tokenized_lists(self, toklist):
        """
        Takes a list of lists of word tokens, and generates the vocabulary based
        on those words.

        :param toklist: (list of lists of strings)
        """
        print("Extracting the vocab from a tokenized list")
        self.vocab = dict()
        for sentence in toklist:
            for word in sentence:
                # If the word exists in wordcount, increment the value by 1. Otherwise
                # create a new key, initialised to 0, and increment by 1.
                self.vocab[word] = self.vocab.get(word, 0) + 1

        self.vocab = Series(self.vocab)
        self.vocab.sort_values(ascending=False, inplace=True)
        self.vocab = concat([Series({u"UNKNOWN":0}), self.vocab], ignore_index=False)
        self.w2i = Series(range(self.vocab.size), index=self.vocab.index)
        self.i2w = self.vocab.index
        self.size = self.vocab.size
        print("---Done!")
