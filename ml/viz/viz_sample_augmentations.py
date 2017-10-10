import os
import numpy as np

# DEPENDS ON
# array2pil()
# batch2grid()

def viz_sample_augmentations(X, aug_func, n_images=5, n_per_image=5, saveto=None):
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
