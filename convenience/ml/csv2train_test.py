from sklearn.cross_validation import train_test_split
import numpy as np
from csv2arrays import csv2arrays
__author__ = 'ronny'


def csv2train_test(file, y_col=None, test=0.3,
           sep=",",
           skip_header=0, skip_footer=0,
           missing_values={"NA", "NAN", "N/A"},
           filling_values=np.nan,
           seed=None):
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

