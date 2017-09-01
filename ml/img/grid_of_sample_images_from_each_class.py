import numpy as np


# ==============================================================================
#                                          GRID_OF_SAMPLE_IMAGES_FROM_EACH_CLASS
# ==============================================================================
def grid_of_sample_images_from_each_class(X, Y, num_per_class=5, seed=None):
    """
    Given a batch of images (stored as a numpy array), and an array of labels,
    It creates a grid of images (randomly sampled), such that:

        - Each row contains images for each class.
        - Each column contains `num_per_class` randomly sampled images for
          that particular class.

    Args:
        X: (numpy array)
            Shape should be either:
                - [n_batch, im_rows, im_cols]
                - [n_batch, im_rows, im_cols, n_channels]

        Y: (list or numpy array)
            The class labels for each sample.

        num_per_class:  (int)
            The number of images to sample for each class.

        param seed: (int)
            Set the random seed.

    Returns: (numpy array)
        The grid of images as one large image of either shape:
            - [n_classes*im_cols, num_per_class*im_rows]
            - [n_classes*im_cols, num_per_class*im_rows, n_channels]

    """
    # TODO: have a resize option to rescale the individual sample images
    # Set the random seed if needed
    assert len(X) == len(Y), "X, and Y should have same number of samples"
    if seed is not None:
        np.random.seed(seed=seed)

    # Dimensions of the grid.
    n_classes = max(Y)+1
    im_shape = X[0].shape
    im_width = im_shape[1]
    im_height = im_shape[0]
    if len(im_shape)>2:
        n_channels = im_shape[2]
        grid_shape = (im_height * n_classes, im_width * num_per_class, n_channels)
    else:
        grid_shape = (im_height * n_classes, im_width * num_per_class)

    # Initialise the grid array
    grid_array = np.zeros(grid_shape, dtype=X[0].dtype)

    # For each class, sample num_per_class images and place them in grid
    for class_i in range(n_classes):
        available_pool = np.argwhere(np.squeeze(Y) == class_i).flatten()
        if len(available_pool) > 0:
            sample_indices = np.random.choice(available_pool, size=min(num_per_class, len(available_pool)), replace=False)
        else:
            # No samples available for this class
            continue

        # Append to corresponding position on grid
        for j, sample_index in enumerate(sample_indices):
            # Skip column if there is not enough samples from for this class
            if j >= len(available_pool):
                break
            row = im_height*class_i
            col = im_width*j

            grid_array[row:row+im_height, col:col+im_width] = X[sample_index]

    return grid_array
