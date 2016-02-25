import numpy as np

__author__ = 'ronny'


# ==============================================================================
#                                                                     CSV2ARRAYS
# ==============================================================================
def csv2arrays(file, sep=",", skip_header=0, skip_footer=0,
               missing_values={"NA", "NAN", "N/A"}, filling_values=np.nan):
    """
    Takes a csv file an d creates an array of the data.

    :param file: {string}
        file path to the csv file
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
    :return: {numpy array}
        A numpy array
    """
    # ==============================================================================
    data = np.genfromtxt(file, delimiter=sep,
                         skip_header=skip_header,
                         skip_footer=skip_footer,
                         missing_values=missing_values,
                         filling_values=filling_values
                        )
    return data

