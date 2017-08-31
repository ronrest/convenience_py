import numpy as np


# ==============================================================================
#                                                           WINIT_SD_RANDOM_WALK
# ==============================================================================
def Winit_sd_random_walk(num_inputs):
    """
    Calculate the Standard Deviation to be used for the distribution of
    values when initialising Weights for ReLus layers.

    Based on Sussillo & Abbot's (2015) Random Walk Initialization algorithm
    Implementation derived from the _random_walk() function found at:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/init_ops.py


    :param num_inputs: {int}
        number of elements in the previous layer
    :return: {float}
        standard deviation to use.
    """
    # ==========================================================================
    g = np.sqrt(2.0) * np.exp(1.2 / (np.max([num_inputs, 6]) - 2.4))
    sd = g / np.sqrt(num_inputs)
    return sd

