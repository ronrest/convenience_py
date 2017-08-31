import numpy as np

__author__ = 'ronny'


# ==============================================================================
#                                                                     CSV2ARRAYS
# ==============================================================================
def csv2arrays(file, y_col=None, shuffle=False,
               sep=",", skip_header=0, skip_footer=0,
               missing_values={"NA", "NAN", "N/A"},
               filling_values=np.nan,
               seed=None):
    """
    Takes a csv file and creates a tuple of arrays containing the data.
    (X, Y)

    :param file: {string}
        file path to the csv file
    :param y_col: {int}(default=None)
        The column in the data containing the output labels. If this file
        doesnt contain any output labels, then use None.
    :param shuffle: {boolean}(defualt=False)
        Should it shuffle the order of the rows?
    :param sep: {str}(default=",")
        delimiter used to separate columns.
    :param skip_header: {int}(default=0)
        Skip this many rows from the top
    :param skip_footer: {int}(default=0)
        Skip this many rows from the end.
    :param missing_values: {set of strings} (default={"NA", "NAN", "N/A"})
        The set of characters to recognise as missing values
    :param filling_values: (default = np.nan)
        what to replace missing values with.
    :param seed: {int or None}(default = None)
        Set the random seed if you want reproducible results
    :return: {numpy arrays}
        If y_col is not None, then it returns a tuple of numpy arrays
            X, Y
        If y_col is None, then it returns a single array
    """
    # ==============================================================================
    data = np.genfromtxt(file, delimiter=sep,
                         skip_header=skip_header,
                         skip_footer=skip_footer,
                         missing_values=missing_values,
                         filling_values=filling_values
                        )

    # Set random seed for reproducible results
    if seed is not None:
        np.random.seed(seed)

    # Get the indices that would shuffle the data
    row_indices = np.random.permutation(data.shape[0]) if shuffle \
        else np.arange(data.shape[0])

    # Split into input data and output labels if there is an output column.
    if y_col is not None:
        x_cols = range(data.shape[1])
        x_cols.pop(y_col)
        X_train = data[:, x_cols]
        Y_train = data[:, y_col]
        return X_train[row_indices,:], Y_train[row_indices]
    else:
        return data[row_indices,:]


