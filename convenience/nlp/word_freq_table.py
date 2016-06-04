import pandas as pd
import collections

# ==============================================================================
#                                                                WORD_FREQ_TABLE
# ==============================================================================
def word_freq_table(docs):
    """
    Takes a list of documents that have been tokenised into a list of words, and
    returns a pandas dataframe that contains the word counts within each
    document.

    :param docs: (list of list of strings)
        A list of lists. each inner list represents the content of the document,
        and it should be composed of tokenized words.
    :return:
        A dataframe table with word counts for each document. The columns have
        the words, and the rows are the different documents
    :example:
        >>> reviews = [['i', 'liked', 'it'],
        >>>            ['i', 'hated', 'it'],
        >>>            ['so', 'so', 'boring'],
        >>>            ['so', 'good']]
        >>> print(word_freq_table(reviews))

           boring  good  hated  i  it  liked  so
        0       0     0      0  1   1      1   0
        1       0     0      1  1   1      0   0
        2       1     0      0  0   0      0   2
        3       0     1      0  0   0      0   1
    """
    # ==========================================================================
    df = [[]] * len(docs)  # List to hold the tallies for each document

    # For each document, create a tally of the words that appear in it
    df = [collections.Counter(doc) for doc in docs]

    # Create a dataframe from the counter objects (and replace NAs with 0s)
    df = pd.DataFrame(df)
    df.fillna(0, inplace=True)

    return df

