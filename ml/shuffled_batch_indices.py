import numpy as np


__author__ = 'Ronny Restrepo'


# ==============================================================================
#                                                         SHUFFLED_BATCH_INDICES
# ==============================================================================
def shuffled_batch_indices(d_size, b_size, n):
    """
    Create a 2D array, where each row contains an array of randomise indices
    from the training data to use for that batch.

    There is the possibility that for any particular batch, there will be one or
    more duplicate indices from the training data. But, over the entire set of
    batches, all training samples will have been sampled the same number of
    times (with maybe some values being sampled one more time than others if:
        `(b_size * n) % d_size != 0`.

    :param d_size: {int}
        Number of samples in training data.
    :param b_size: {int}
        Batch size.
    :param n: {int}
        Number of batches.
    :return: {2D array}
        2D array, such that array[0] returns the indices for the first batch.
    """
    # ==========================================================================
    indices = np.random.permutation(b_size * n)
    indices = np.array([index % d_size for index in indices])
    return indices.reshape(-1, b_size)


