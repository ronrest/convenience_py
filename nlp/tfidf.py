# import io
# import numpy as np
# import pandas as pd

from collections import OrderedDict

from nltk.tokenize import RegexpTokenizer
from gensim import corpora, models
#import gensim


class TFIDF(object):
    def __init__(self):
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.vocab = corpora.Dictionary()
        self.tfidf = models.TfidfModel(dictionary=self.vocab, smartirs=None) # smartirs="ntn" or "ntc"
        # self.tfidf.dfs      # DOcument Frequencies
        # self.tfidf.dfs[4]   # DOcument Frequencies
        # self.tfidf.idfs     # Inverse Document Frequencies
        # self.tfidf.idfs[4]  # Inverse Document Frequencies

    @property
    def n_vocab(self):
        """ return the size of the vocab"""
        return len(self.vocab)

    def save(self, filename):
        # tfidf.save()
        self.vocab.save_as_text("{}.vocab".format(filename))
        print("WARNING: only vocab saved")
        # self.tfidf.save("{}.vocab".tfidf(filename))

    def load(self, filename):
        self.vocab = self.vocab.load_from_text("{}.vocab".format(filename))
        self.fit_from_vocab()
        print("WARNING: only vocab loaded, tfidf object fitted from vocab")

    def id2str(id):
        return self.vocab.id2token[id]

    def str2id(self, s):
        return self.vocab.token2id[s]
        # dictionary.token2id["banana"]

    def df(self, s):
        """ Given a token string, it returns the number of documents it appears in """
        return self.vocab.dfs[self.str2id(s)]

    def tokenize(self, s):
        return self.tokenizer.tokenize(s.lower())

    def doc2ids(self, s):
        """ Given a string document it tokenizes and converts to list of ids"""
        return self.vocab.doc2idx(self.tokenize(s))

    def doc2bow(self, s, sort=False, string_keys=True, as_dict=True):
        """ Given a document string it tokenizes and returns a bag of words
            represented in sparse format, as a list of
            (token_id, token_count) tuples

            TODO: option for:
            - dictionary
            - sorted
            - as string tokens
        """
        scores = self.vocab.doc2bow(self.tokenize(s))
        if sort:
            # Order by tfidf score from highest to lowest
            scores = sorted(scores, key=lambda x: x[1], reverse=True)
        if string_keys:
            # Use the string representation of the tokens instead of integer id
            scores = [(self.vocab[token],score) for token, score in scores]
        if as_dict:
            # Convert to a dict instead of list of 2-tuple pairs
            scores = OrderedDict(scores)
        return scores

    def extend_vocab(self, docs):
        """ Given an iterable of string documents, it tokenizes the documents
            and adds the new words to the vocab.
        """
        for doc in docs:
            doc = self.tokenize(doc)
            self.vocab.add_documents([doc])

    def trim_vocab(self, min_count=5, max_freq=0.5, top_n=1000000, keep_tokens=None, remove_numeric=True, remove_tokens=None):
        """
        min_count: (int) only keep tokens that occur in at least this many documents
        max_freq: (float) filter out common tokens that appear more frequently
                than in this proportion of documents.
        top_n: (int) Only keep the top_n most frequent tokens
        keep_tokens: list of tokens to keep in the vocab, **no matter what**
        remove_numeric: remove tokens that are just numbers (ints or floats)
        remove_tokens: tokens to remove, no matter what.

        TODO: remove wallet hash addresses from vocab
        """
        if remove_numeric:
            self.remove_numeric_tokens()
        if remove_tokens is not None:
            self.remove_tokens(remove_tokens)
        self.vocab.filter_extremes(no_below=min_count, no_above=max_freq,
                                   keep_n=top_n, keep_tokens=keep_tokens)

    def remove_numeric_tokens(self):
        """ Removes tokens that are just numbers """
        def is_float_string(s):
            """ Returns True if string can be converted to a float"""
            try:
                float(s)
                return True
            except ValueError:
                return False

        bad_tokens = [val for val in self.vocab.values() if is_float_string(val)]
        self.remove_tokens(bad_tokens)

    def remove_tokens(self, tokens):
        """ Given a list of token strings, it removes them from the vocab"""
        bad_token_ids = self.vocab.doc2idx(tokens)
        self.vocab.filter_tokens(bad_ids=bad_token_ids)

    # def fit(self, docs):
    #     """Given an iterable of strings, it creates the TFIDF object """
    #     self.tfidf = models.TfidfModel(docs)

    def fit_from_vocab(self, method="ltc"):
        """ Given an iterable of strings, it creates the TFIDF object
        Args:
            method: String with three characters, eg "ltc", "ntc", which
                    correspond to the following:

                Term frequency weighing:
                    * `n` - natural,
                    * `l` - logarithm,
                    * `a` - augmented,
                    * `b` - boolean,
                    * `L` - log average.

                Document frequency weighting:
                    * `n` - none,
                    * `t` - idf,
                    * `p` - prob idf.

                Document normalization:
                    * `n` - none,
                    * `c` - cosine.
        """
        self.tfidf = models.TfidfModel(dictionary=self.vocab, smartirs=method) # smartirs="ntn" or "ntc"


    def doc2tfidf(self, doc, as_dict=True, string_keys=True, sort=True, min_count=None):
        """ Given a string, it returns a mapping from token to tfidf score.
            Depending on arguments passed, it returns either a list of
            (token, tfidf_score) tuples, or a dictionary of {token, tfidf_score}
            pairs.
            Can optionally chose to return either tokens represented as token ids,
            or as their string representation.
        Args:
            s:  (str) the string to process
            as_dict: (bool)
                - If True, return as an ordered dict of {token: tfidf_score}
                  pairs.
                - If False, return as a list of (token, tfidf_score) pairs
            string_keys: (bool)
                - If True, then the token is represented by it's string
                - If False, then the token is represented by its integer id
            sort: (bool) sort the items by descending tfidf values?
        Returns:
            scores:
        """
        doc = doc.lower()
        tokens = self.tokenizer.tokenize(doc)   # tokenize string

        bow = self.vocab.doc2bow(tokens) # bag of words of tokens
        # filter tokens that do not occur a minimum amount of times
        if min_count is not None:
            bow = [(k,v) for k,v in bow if v >= min_count]
        scores = self.tfidf[bow] # a list of (token_id, tfidf_score) tuples
        if sort:
            # Order by tfidf score from highest to lowest
            scores = sorted(scores, key=lambda x: x[1], reverse=True)
        if string_keys:
            # Use the string representation of the tokens instead of integer id
            scores = [(self.vocab[token],score) for token, score in scores]
        if as_dict:
            # Convert to a dict instead of list of 2-tuple pairs
            scores = OrderedDict(scores)
        return scores



# ##############################################################################
#                                                  usage
# ##############################################################################
# from tfidf import TFIDF
# tiffy = TFIDF()
# tiffy.extend_vocab(docs) # where docs is an iterable of strings
# tiffy.extend_vocab([""]) # to prevent some words occuring 100% of time
# tiffy.trim_vocab(min_count=5, max_freq=1.0, top_n=1000000, remove_numeric=True, keep_tokens=keepers, remove_tokens=stopwords)
# tiffy.fit_from_vocab(method=None)
# # tiffy.fit_from_vocab(method="ltc")
# tiffy.n_vocab # size of vocab

## Save the vocab
# tiffy.save("vocab")

# create tfidf scores from a string
# tfidf_scores = tiffy.doc2tfidf(
#                 doc=docs.loc[day],
#                 as_dict=True,
#                 string_keys=True,
#                 sort=True,
#                 min_count=5,
#                 )

# create a bag of words from a string (as a dict)
# bow = tiffy.doc2bow("bitcoin delist orange cookies cookies delist", sort=True, string_keys=True, as_dict=True)

# # loading vocab from saved file, then fitting tfidf from vocab
# tiffy.load("vocab")
# tiffy.fit_from_vocab(method=None)
