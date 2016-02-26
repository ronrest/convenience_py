from sklearn.cross_validation import train_test_split
import numpy as np
from csv2arrays import csv2arrays
__author__ = 'ronny'


# ==============================================================================
#                                                                 CSV2TRAIN_TEST
# ==============================================================================
def csv2train_test(file, y_col=None, test=0.3,
           sep=",",
           skip_header=0, skip_footer=0,
           missing_values={"NA", "NAN", "N/A"},
           filling_values=np.nan,
           seed=None):
    """
    Takes a csv file and creates a tuple of arrays containing the data.
        X_train, Y_train, X_test, Y_test
    or if no y_col is specified, then:
        X_train, X_test

    NOTE: The rows are automatically shuffled.

    :param file: {string}
        file path to the csv file
    :param y_col: {int}(default=None)
        The column in the data containing the output labels. If this file
        doesnt contain any output labels, then use None.
    :param test: {float greater than 0.0 and less than 1.0}(default=0.3)
        proportion of the data to assign to the test set.
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
    :return: {tuple of numpy arrays}
        If a y_col is specified, then it returns
            X_train, Y_train, X_test, Y_test
        Otherwise it returns:
            X_train, X_test
    """
    # ==========================================================================
    data = csv2arrays(file=file, y_col=y_col, shuffle=False,
               sep=sep,
               skip_header=skip_header, skip_footer=skip_footer,
               missing_values=missing_values,
               filling_values=filling_values,
               seed=seed)

    if y_col is None:
        return train_test_split(data, test_size=test, random_state=seed)
    else:
        X_train, X_test, \
        Y_train, Y_test = train_test_split(data[0], data[1], test_size=test,
                                           random_state=seed)
        return X_train, Y_train, X_test, Y_test

