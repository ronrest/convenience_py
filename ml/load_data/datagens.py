import numpy as np

def np_generator(x, y, batch_size=32, shuffle=False):
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


