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


def text_file_line_generator(path, skip_first_line=False):
    """ A generator that loads one line of a file at a time, and loops
        the file infinitely.

        Optionally allows you to skip the first line, eg in the case of a
        csv file that contains the csv header of column names.

    NOTE:
        It also skips any lines with only whitespaces.

    TODO: Find if there is a way to randomise the order of line reads.
    """
    while True:
        with open(path, "r") as fileobj:
            firstline = True
            for line in fileobj:
                if firstline and skip_first_line:
                    firstline=False
                    continue
                line = line.strip()
                if line == "":
                    continue
                else:
                    yield line


