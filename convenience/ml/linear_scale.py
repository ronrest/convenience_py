import numpy as np


def linear_scale(x, new_range=(0.0, 1.0), old_range="auto"):
    if old_range is "auto":
        old_range = (x.min(), x.max())

    old_min = old_range[0]
    old_max = old_range[1]

    new_min = new_range[0]
    new_max = new_range[1]

    # The scaling ratio
    ratio = float(new_max - new_min) / old_max - old_min

    # Scale values to the new range of values
    return new_min + ratio*(np.array(x) - old_min)


