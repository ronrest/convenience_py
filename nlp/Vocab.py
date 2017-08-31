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

    # ==========================================================================
    #                                                                 INDEX2WORD
    # ==========================================================================
    def index2word(self, indices):
        """
        Takes an integer or list of integers reresenting indices, and returns
        a list of strings for each of the corresponding tokens in the vocab.

        :param indices: (int, or list of ints)
        :return: (list of strings)
        """
        if isinstance(indices, int):
            indices = [indices]
        return list(self.i2w[indices])

    # ==========================================================================
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


    # ==========================================================================
    #                                                                 LIMIT_SIZE
    # ==========================================================================
    def limit_size(self, n):
        """
        Limit the size of the vocabulary to n number of tokens. Any word counts
        for words that get trimmed off will be summed and added to the "UNKNOWN"
        token.

        :param n: (int)
            Max size of the vocabulary.
        """
        print("Triming the vocab size to: {} tokens".format(n))
        rem = self.vocab[range(n, len(self.vocab))] # Items to be removed
        rem_sum = rem.sum()                 # Sum of values for items removed
        self.vocab["UNKNOWN"] += rem_sum    # Removed words become unknown words
        self.vocab = self.vocab.head(n)     # items to keep
        self.size = n                       # update the size of the vocab
        self.i2w = self.i2w[:n]
        self.w2i  = self.w2i.head(n)
        print("--- Done!")


    # ==========================================================================
    #                                                                REMOVE_RARE
    # ==========================================================================
    def remove_rare(self, min):
        """
        Remove tokens that occur less than min number of times.

        :param min: (int)
            Min frequency count. Tokens with frequency counts less than this
            are discarded (and treated as "UNKNOWN" words).
        """
        print("Removing rare tokens with counts less than {}".format(min))
        rem = self.vocab[self.vocab < min]     # Items to be removed
        rem_sum = rem.sum()                    # Sum of values for items removed
        self.vocab["UNKNOWN"] += rem_sum       # Removed words become UNKNOWN

        keepers = self.vocab >= min
        self.vocab = self.vocab[keepers]        # Items to keep

        self.size = self.vocab.size             # update the size of the vocab
        self.i2w = self.i2w[:self.size]
        self.w2i = self.w2i.head(self.size)
        print("--- Done!")


