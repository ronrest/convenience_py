import numpy as np

__author__ = 'ronny'


def sample_grid_of_arrays(X, Y, num_per_class=5, seed=None):
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

