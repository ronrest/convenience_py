import numpy as np

def calculate_class_weights(Y, n_classes, method="paszke", c=1.02):
    # CLASS PROBABILITIES - based on empirical observation of data
    ids, counts = np.unique(Y, return_counts=True)
    n_pixels = Y.size
    p_class = np.zeros(n_classes)
    p_class[ids] = counts/n_pixels

    # CLASS WEIGHTS
    if method == "paszke":
        weights = 1/np.log(c+p_class)
    elif method == "eigen":
        assert False, "TODO: Implement eigen method"
        # TODO: Implement eigen method
        # where class_freq is the number of pixels of class c divided by
        # the total number of pixels in images where c is actually present,
        # and median freq is the median of these frequencies.
    elif method in {"eigen2", "logeigen2"}:
        epsilon = 1e-8 # to prevent division by 0
        median = np.median(p_class)
        weights = median/(p_class+epsilon)
        if method == "logeigen2":
            weights = np.log(weights+1)
    else:
        assert False, "Incorrect choice for method"

    return weights
