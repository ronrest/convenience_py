import numpy as np

__author__ = 'ronny'


def csv2arrays(file, sep=",", skip_header=0, skip_footer=0,
               missing_values={"NA", "NAN", "N/A"}, filling_values=np.nan):
    data = np.genfromtxt(file, delimiter=sep,
                         skip_header=skip_header,
                         skip_footer=skip_footer,
                         missing_values=missing_values,
                         filling_values=filling_values
                        )
    return data

