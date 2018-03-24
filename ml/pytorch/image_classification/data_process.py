import os
import pickle
import numpy as np
from image_process import  nhwc2nchw

def pickle2obj(file):
    """ Loads the contents of a pickle as a python object. """
    with open(file, mode = "rb") as fileObj:
        obj = pickle.load(fileObj)
        return obj

def preprocess_images(x,y):
    x = x/255.0          # Scale to be between 0-1
    x = nhwc2nchw(x)     # COnvert images to NCHW format for pytorch
    return x, y

def data_generator(x, y, preprocess_func=None, batch_size=32, shuffle=False):
    rawgen = np_datagen(x, y, batch_size=batch_size, shuffle=shuffle)
    while True:
        x,y = next(rawgen)
        if preprocess_func is not None:
            x,y = preprocess_func(x,y)
        yield x,y

def np_datagen(x, y, batch_size=32, shuffle=False):
    """ Given two numpy arrays representing inputs and output-target labels,
        it creates a python data generator that will loop through this data
        infinitely and return batches of x,y pairs.

        TODO: Add a random seed
    """
    assert len(y) == len(x), "First dimension of x and y arrays must be the same"
    n_samples = len(y)
    n_steps = n_samples // batch_size
    while True:
        if shuffle:
            shuffled_indices = np.random.permutation(n_samples)
            x = x[shuffled_indices]
            y = y[shuffled_indices]
        for i in range(n_steps):
            x_batch = x[i*batch_size: (i+1)*batch_size]
            y_batch = y[i*batch_size: (i+1)*batch_size]
            yield x_batch, y_batch


def create_valid_split(data, n_valid):
    """ Create validation data from the training data """
    data["X_valid"] = data["X_train"][:n_valid]
    data["Y_valid"] = data["Y_train"][:n_valid]
    data["X_train"] = data["X_train"][n_valid:]
    data["Y_train"] = data["Y_train"][n_valid:]
