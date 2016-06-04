import pandas as pd
import collections

def word_freq_table(docs):
    df = [[]] * len(docs)  # List to hold the tallies for each document

    # For each document, create a tally of the words that appear in it
    df = [collections.Counter(doc) for doc in docs]

    # Create a dataframe from the counter objects (and replace NAs with 0s)
    df = pd.DataFrame(df)
    df.fillna(0, inplace=True)

    return df

