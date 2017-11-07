import numpy as np


# ==============================================================================
#                                                                   BATCH 2 GRID
# ==============================================================================
def batch2grid(imgs, rows, cols):
    """
    Given a batch of images stored as a numpy array of shape:

           [n_batch, img_height, img_width]
        or [n_batch, img_height, img_width, n_channels]

    it creates a grid of those images of shape described in `rows` and `cols`.

    Args:
        imgs: (numpy array)
            Shape should be either:
                - [n_batch, im_rows, im_cols]
                - [n_batch, im_rows, im_cols, n_channels]

        rows: (int) How many rows of images to use
        cols: (int) How many cols of images to use

    Returns: (numpy array)
        The grid of images as one large image of either shape:
            - [n_classes*im_cols, num_per_class*im_rows]
            - [n_classes*im_cols, num_per_class*im_rows, n_channels]
    """
    # TODO: have a resize option to rescale the individual sample images
    # TODO: Have a random shuffle option
    # TODO: Set the random seed if needed
    assert rows>0 and cols>0, "rows and cols must be positive integers"

    # Prepare dimensions of the grid
    n_cells = (rows*cols)
    imgs = imgs[:n_cells] # Only use the number of images needed to fill grid
    n_samples, img_height, img_width, n_channels = imgs.shape

    # Image dimensions
    n_dims = imgs.ndim
    assert n_dims==3 or n_dims==4, "Incorrect # of dimensions for input array"

    # Deal with images that have no color channel
    if n_dims == 3:
        imgs = np.expand_dims(imgs, axis=3)

    # Handle case where there is not enough images in batch to fill grid
    if n_cells > n_samples:
        n_gap = n_cells - n_samples
        imgs = np.pad(imgs, pad_width=[(0,n_gap),(0,0), (0,0), (0,0)], mode="constant", constant_values=0)

    # Reshape into grid
    grid = imgs.reshape(rows, cols,img_height,img_width,n_channels).swapaxes(1,2)
    grid = grid.reshape(rows*img_height,cols*img_width,n_channels)

    # If input was flat images with no color channels, then flatten the output
    if n_dims == 3:
        grid = grid.squeeze(axis=2) # axis 2 because batch dim has been removed

    return grid
