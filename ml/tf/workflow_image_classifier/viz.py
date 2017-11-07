import numpy as np
import matplotlib
matplotlib.use('AGG') # make matplotlib work on aws
import matplotlib.pyplot as plt

__author__ = "Ronny Restrepo"
__copyright__ = "Copyright 2017, Ronny Restrepo"
__credits__ = ["Ronny Restrepo"]
__license__ = "Apache License"
__version__ = "2.0"


# ==============================================================================
#                                                                   TRAIN_CURVES
# ==============================================================================
def train_curves(train, valid, saveto=None, title="Accuracy over time", ylab="accuracy", legend_pos="lower right"):
    """ Plots the training curves. If `saveto` is specified, it saves the
        the plot image to a file instead of showing it.
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.suptitle(title, fontsize=15)
    ax.plot(train, color="#FF4F40",  label="train")
    ax.plot(valid, color="#307EC7",  label="valid")
    ax.set_xlabel("epoch")
    ax.set_ylabel(ylab)

    # Grid lines
    ax.grid(True)
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='#888888', linestyle='-')
    plt.grid(b=True, which='minor', color='#AAAAAA', linestyle='-', alpha=0.2)

    # Legend
    ax.legend(loc=legend_pos, title="", frameon=False,  fontsize=8)

    # Save or show
    if saveto is None:
        plt.show()
    else:
        fig.savefig(saveto)
        plt.close()


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


# ==============================================================================
#                                                                      ARRAY2PIL
# ==============================================================================
def array2pil(x):
    """ Given a numpy array containing image information returns a PIL image.
        Automatically handles mode, and even handles greyscale images with a
        channels axis
    """
    if x.ndim == 2:
        mode = "L"
    elif x.ndim == 3 and x.shape[2] == 1:
        mode = "L"
        x = x.squeeze()
    elif x.ndim == 3:
        mode = "RGB"
    return PIL.Image.fromarray(x, mode=mode)


# ==============================================================================
#                                                       VIZ_SAMPLE_AUGMENTATIONS
# ==============================================================================
def viz_sample_augmentations(X, aug_func, n_images=5, n_per_image=5, saveto=None):
    """ Given a batch of data X, and Y,  it takes n_images samples, and performs
        `n_per_image` random transformations for segmentation data on each of
        those images. It then puts them in a grid to visualize. Grid size is:
            n_images wide x n_per_image high

    Args:
        X:          (np array) batch of images
        aug_func:   (func) function with API `aug_func(X, Y)` that performs
                    random transformations on the images for segmentation
                    purposes.
        n_images:   (int)
        n_per_image:(int)
        saveto:     (str or None)

    Returns: (None, or PIL image)
        If saveto is provided, then it saves teh image and returns None.
        Else, it returns the PIL image.
    Examples:
        samples = viz_sample_seg_augmentations(data["X_train"], data["Y_train"],
            aug_func=aug_func, n_images=5, n_per_image=5, saveto=None)
        samples.show()
    """
    X = X[:n_images]
    grid = []

    # Perform Augmentations
    for col in range(n_per_image):
        x = aug_func(X)
        grid.append(x)

    # Put into a grid
    _, height, width, n_channels = X.shape
    grid = np.array(grid, dtype=np.uint8).reshape(n_images*n_per_image, height, width, n_channels)
    grid = batch2grid(grid, n_per_image, n_images)

    # Convert to PIL image
    grid = array2pil(grid)

    # Optionally save image
    if saveto is not None:
        # Create necessary file structure
        pardir = os.path.dirname(saveto)
        if pardir.strip() != "": # ensure pardir is not an empty string
            if not os.path.exists(pardir):
                os.makedirs(pardir)
        grid.save(saveto, "JPEG")

    return grid
