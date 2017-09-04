import numpy as np


# ==============================================================================
#                                                        BATCH_OF_IMAGES_TO_GRID
# ==============================================================================
def batch_of_images_to_grid(imgs, rows, cols):
    """
    Given a batch of images stored as a numpy array of shape:
        [n_batch, img_height, img_width, n_channels]
    it creates a grid of images of shape described in `rows` and `cols`.

    Args:
        imgs: (numpy array)
            Shape should be:
                - [n_batch, im_rows, im_cols, n_channels]

        rows: (int) How many rows of images to use
        cols: (int) How many cols of images to use

    Returns: (numpy array)
        The grid of images as one large image of shape:
            - [n_classes*im_cols, num_per_class*im_rows, n_channels]
    """
    # TODO: handle case where images have no color chanels (greyscale)

    # TODO: have a resize option to rescale the individual sample images
    # Set the random seed if needed

    # TODO: Have a random shuffle option
    # if seed is not None:
    #     np.random.seed(seed=seed)

    # Only use the number of images needed to fill grid
    n_cells = (rows*cols)
    imgs = imgs[:n_cells]

    n_batch, img_height, img_width, n_channels = imgs.shape

    # Handle case where there is not enough images in batch to fill grid
    n_gap = n_cells - n_batch
    imgs = np.pad(imgs, pad_width=[(0,n_gap),(0,0), (0,0), (0,0)], mode="constant", constant_values=0)

    # Reshape into grid
    grid = imgs.reshape(rows,cols,img_height,img_width,n_channels).swapaxes(1,2)
    grid = grid.reshape(rows*img_height,cols*img_width,n_channels)

    return grid
