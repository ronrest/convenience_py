import os
import numpy as np

# DEPENDS ON
# array2pil()
# batch2grid()

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
