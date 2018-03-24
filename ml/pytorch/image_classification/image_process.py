import numpy as np

def nhwc2nchw(x):
    """ Given an array of images as NHWC it converts to NCHW format """
    return np.moveaxis(x, [0,1,2,3], [0,2,3,1])
