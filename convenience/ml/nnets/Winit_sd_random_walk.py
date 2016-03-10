import numpy as np

def Winit_sd_random_walk(num_inputs):
    g = np.sqrt(2.0) * np.exp(1.2 / (np.max([num_inputs, 6]) - 2.4))
    sd = g / np.sqrt(num_inputs)
    return sd
