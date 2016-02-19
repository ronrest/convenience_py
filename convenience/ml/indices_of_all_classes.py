__author__ = 'Ronny Restrepo'

import numpy as np

def indices_of_all_classes(y):
    return {i: np.where(y == i)[0] for i in np.unique(y)}

