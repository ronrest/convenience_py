import numpy as np

__author__ = 'ronny'


# ==============================================================================
#                                                          SAMPLE_GRID_OF_ARRAYS
# ==============================================================================
def sample_grid_of_arrays(X, Y, num_per_class=5, seed=None):
    """
    Useful for image processing tasks.

    Takes a 3D dataset X which can be thought of as a stack (or rows) of 2D
    arrays. Also takes a 1D array Y which is the output class labels for each 2D
    array. It then returns a big 2D array, which can be though of as a grid
    of a bunch of the original 2D arrays.

    Each row along this grid, represents each of the output classes.
    Each column of the grid is a random sample for a specific class.
    You can specify the number of samples (columns on the grid) from each class
    using the `num_per_class` argument.

    If the data in X is image data, then it can be though of as creating a grid
    of images, with rows of images from each class.

    :param X: {3D array}
        Array to be thought of as a a stack of 2D arrays
    :param Y: {1D array}
        Output labels for each 2D array in X.
    :param num_per_class: {int}
        Number of samples (columns) for each class to randomly sample.
    :param seed: {int}
        Set the random seed.
    :return: {2D array}
        A 2D array that is to be thought of as a grid of the sampled 2D arrays
        for each class.
    """
    # ==========================================================================
    # TODO: have a resize option to resize from a 2D array to a 3D array.

    # Set the random seed if needed
    if seed is not None:
        np.random.seed(seed=seed)

    # Dimensions of the grid of arrays.
    cell_width = X[0].shape[1]
    cell_height = X[0].shape[0]

    # Indices of all classes in dataset
    class_indices = {i: np.where(Y == i)[0] for i in np.unique(Y)}
    num_classes = len(class_indices.keys())

    # Initialise the big grid array
    grid_array = np.empty(shape=(cell_height * num_classes,
                                 cell_width * num_per_class), dtype=float)

    # Loop through each class
    for i, label in enumerate(class_indices):
        indices_of_class_i = class_indices[i]

        # Take a sample of n random array element indexes
        sample_indices = np.random.choice(indices_of_class_i,
                                          size=num_per_class, replace=False)

        # For each of those indices, append the corresponding 2D array from `X`
        # to the corresponding portion of `grid_array` to generate a grid
        # composed of 2D arrays.
        for j, sample_index in enumerate(sample_indices):
            grid_array[cell_height*i: cell_height*i + cell_height,
                       cell_width*j: cell_width*j+ cell_width] = X[sample_index]

    return grid_array


