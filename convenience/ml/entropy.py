import numpy as np

def entropy(x):
    p = x/x.sum()                   # probability for each class
    return (-p*np.log2(p)).sum()    # return entropy

