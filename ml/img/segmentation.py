import PIL
import PIL.Image
import numpy as np
import os

# ==============================================================================
#                                                         VIZ_SEGMENTATION_LABEL
# ==============================================================================
def viz_segmentation_label(label, colormap=None, saveto=None):
    """ Given a 2D numpy array representing a segmentation label, with
        the pixel value representing the class of the object, then
        it creates an RGB PIL image that color codes each label.

    Args:
        label:          (numpy array) 2D flat image where the pixel value
                        represents the class label.
        colormap:   (list of lists of 3 ints)
                        A list where each index represents the RGB value
                        for the corresponding class id.
                        Eg: to map class_0 to black and class_1 to red:
                            [[0,0,0], [255,0,0]]
                        By default, it creates a map that supports 4 classes:
                        0. black
                        1. guava red
                        2. nice green
                        3. nice blue
        saveto:         (str or None)(default=None)(Optional)
                        File path to save the image to (as a jpg image)
    Returns:
        PIL image
    """
    if colormap is None:
        # Default color mapper
        colormap = [[0,0,0],
                        [255,79,64],
                        [115,173,33],
                        [48,126,199],
                        ]
    # Map each pixel label to a color
    label_viz = np.zeros((label.shape[0],label.shape[1],3), dtype=np.uint8)
    uids = np.unique(label)
    for uid in uids:
        label_viz[label==uid] = colormap[uid]

    # Convert to PIL image
    label_viz = PIL.Image.fromarray(label_viz)

    if saveto is not None:
        # Create necessary file structure
        pardir = os.path.dirname(saveto)
        if pardir.strip() != "": # ensure pardir is not an empty string
            if not os.path.exists(pardir):
                os.makedirs(pardir)
        label_viz.save(saveto, "JPEG")

    return label_viz
