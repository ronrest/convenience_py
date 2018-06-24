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


import csv
def csv_file_line_generator(file, skip=1, packaged=None):
    """ Yields a single line of a csv file. Allows you to open directly from
        a packaged/compressed file.

    Args:
        file:  (str) path to file
        skip:   (int)(default=1)
            lines to skip at begining (by default assumes there is a header
            line that can be skipped)
        packaged: (str| None)
            - `None` assumes it is a text file.
            - `gz` opens the text file wrapped in a `gz` package.
    """
    if packaged is None:
        fileobj = open(file,'rt')
    if packaged == "gz":
        fileobj = gzip.open(file,'rt')

    with fileobj:
        reader = csv.reader(fileobj)
        for i in range(skip):
            _ = next(reader)
        for row in reader:
            yield row

# import csv
def csv2df_line_generator(file, columns=None, skip=1, packaged=None):
    """ Given a path to a csv file, it yields a single line of data as a
        pandas dataframe.

    Args:
        file:  (str) path to file
        columns: (list of strs) column names
        skip:   (int)(default=1)
            lines to skip at begining (by default assumes there is a header
            line that can be skipped)
        packaged: (str| None)
            - `None` assumes it is a text file.
            - `gz` opens the text file wrapped in a `gz` package.
    """
    if packaged is None:
        fileobj = open(file,'rt')
    if packaged == "gz":
        fileobj = gzip.open(file,'rt')

    with fileobj:
        reader = csv.reader(fileobj)
        for i in range(skip):
            _ = next(reader)
        for row in reader:
            yield pd.DataFrame([row], columns=columns)


# import numpy as np
import pandas as pd
import StringIO
def csv_generator(path, x_vars, y_vars,  batch_size=32, x_dtype=np.float32, y_dtype=np.uint8):
    """ Memory efficient way to load data from a csv file, `batch_size` rows
        at a time.

        NOTE: This version will probably not work if the data itself contains newlines.

    Args:
        path:   (str) path to the csv file.
        x_vars: (list of str) the column names to use as input variables
        y_vars: (list of str) the columns name(s) to use as output variables.
                NOTE: it must be in a list, even if it is only one output
                variable.
        batch_size: (int) size of each batch.
        x_dtype: datatype to use for input variables.
        y_dtype: datatype to use for output variables.

    NOTE:
        loads the data as float32 from the csv file before typecasting to
        the specified datatypes.

    Returns:
        X:  (2d numpy array) the batch of inputs
        Y:  (nd numpy array) the class labels
    """
    g = text_file_line_generator(path)
    while True:
        lines = []
        for i in range(batch_size):
            lines.append(next(g))
        batch = "\n".join(lines)
        batch = pd.read_csv(StringIO(batch), header=None, names=x_vars+y_vars, dtype="float32")
        X = batch[x_vars]
        Y = batch[y_vars]
        batch = None # free up some memory
        yield (np.asarray(X, dtype=x_dtype), np.asarray(Y, dtype=y_dtype))
