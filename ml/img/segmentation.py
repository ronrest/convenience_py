import numpy as np


def pixels_with_value(img, val):
    return np.all(img==np.array(val), axis=2)


