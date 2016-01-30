import numpy as np
import pandas as pd

def tally(x, as_df=True):
    cc =np.array(np.unique(x, return_counts=True))
    ratios = cc[1] / float(cc[1].sum())
    table = np.vstack((cc, ratios)).T
    if as_df:
        table = pd.DataFrame(table)
        table.columns = ["value", "count", "ratio"]
        return table
    else:
        return table

