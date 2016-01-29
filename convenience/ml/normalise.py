"""====================================================
                    DESCRIPTION

=======================================================
"""
__author__ = 'ronny'

import numpy as np

def normalise_columns(x, mean, sd):
    return (np.array(x) - mean) / sd


