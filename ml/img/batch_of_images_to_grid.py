import numpy as np


# ==============================================================================
#                                                GRID_OF_IMAGES_FROM_BATCH_ARRAY
# ==============================================================================
def batch_of_images_to_grid(X, rowcol=(3,2), seed=None):
    """
    Given a batch of images (stored as a numpy array), it creates a grid
    of images arranged in `rowcol=(n_rows, n_cols)` images.

    Args:
        X: (numpy array)
            Shape should be either:
                - [n_batch, im_rows, im_cols]
                - [n_batch, im_rows, im_cols, n_channels]


        rowcol: (tuple of two ints)(default=(2,2))
            (rows, cols)

        param seed: (int)
            Set the random seed.

    Returns: (numpy array)
        The grid of images as one large image of either shape:
            - [n_classes*im_cols, num_per_class*im_rows]
            - [n_classes*im_cols, num_per_class*im_rows, n_channels]

    """
    # TODO: have a resize option to rescale the individual sample images
    # Set the random seed if needed
    if seed is not None:
        np.random.seed(seed=seed)

    # Dimensions of the grid.
    rows, cols = rowcol
    im_shape = X[0].shape
    im_width = im_shape[1]
    im_height = im_shape[0]
    if len(im_shape)>2:
        n_channels = im_shape[2]
        grid_shape = (im_height * rows, im_width * cols, n_channels)
    else:
        grid_shape = (im_height * rows, im_width * cols)

    # Initialise the grid array
    grid_array = np.zeros(grid_shape, dtype=X[0].dtype)

    # For each class, sample num_per_class images and place them in grid
    sample_indices = np.random.choice(range(len(X)), size=min(rows*cols, len(X)), replace=False)
    print("num samples imdices", len(sample_indices), sample_indices)
    for i in range(rows):
        for j in range(cols):
            row = i*im_height
            col = j*im_width

            # If not enough data to fill grid, then stop now
            sample_index = i*cols+j
            if sample_index >= len(X):
                break

            # Append to corresponding position on grid
            grid_array[row:row+im_height, col:col+im_width] = X[sample_indices[sample_index]]

    return grid_array
