import numpy as np


# ==============================================================================
#                                          GRID_OF_SAMPLE_IMAGES_FROM_EACH_CLASS
# ==============================================================================
def sample_images_from_each_class(X, Y, n_classes=None, n=5):
    """ Given a batch of images (stored as a numpy array), and an array of
        labels, It creates a grid of images such that:
            - Each row contains images for each class.
            - Each column contains the first `n` images for that class.

    Args:
        X: (numpy array)
            Array containing batch of images. Shape should be:
                - [n_batch, im_rows, im_cols, n_channels]
        Y: (list or numpy array)
            The class labels for each sample.
        n_classes: (int, or None)(default=None)
            The number of classes in the data.
            If this value is `None`, then the number of classes will be
            infered from the max val from Y.
        n:  (int)(default=5)
            The number of images to sample for each class.

    Returns: (numpy array)
        The grid of images as one large image of shape:
            - [n_classes*im_cols, num_per_class*im_rows, n_channels]
    """
    # TODO: maybe add random sampling.
    # TODO: Handle greyscale images with no channels dimension

    cols = n
    _, img_height, img_width, n_channels =  X.shape

    # Infer the number of classes if not provided
    if n_classes is None:
        n_classes = Y.max()

    # Initialize the grid
    grid_shape = (0, img_width * (cols+1), n_channels)
    grid = np.zeros(grid_shape, dtype=np.uint8)

    # FOR EACH CLASS
    for id in range(n_classes):
        # Extract the images for the current class id
        imgs = X[Y==id][:cols]
        row = batch_of_images_to_grid(imgs, rows=1, cols=cols)

        # BOOKMARK: Uncomment these lines to add label images
        # Add a label image (to make it easier to know what each row is)
        # Extract the label image - ignoring alpha channel
        # img_file = os.path.join("images", "{:02d}.png".format(id))
        # label_img = scipy.misc.imread(img_file)[:,:,:3] # Ignore the alpha chanel
        # label_img = scipy.misc.imresize(label_img, [img_height, img_width]) # resize
        # row = np.append(label_img, row, axis=1) # Append label image and samples

        # Append row of samples to the grid
        grid = np.append(grid, row, axis=0)

    return grid
