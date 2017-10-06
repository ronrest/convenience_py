import PIL
import PIL.Image
import PIL.ImageChops
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
        label:      (numpy array) 2D flat image where the pixel value
                    represents the class label.
        colormap:   (list of 3-tuples of ints)
                    A list where each index represents the RGB value
                    for the corresponding class id.
                    Eg: to map class_0 to black and class_1 to red:
                        [(0,0,0), (255,0,0)]
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
    # Default colormap
    if colormap is None:
        colormap = [[0,0,0], [255,79,64], [115,173,33],[48,126,199]]

    # Map each pixel label to a color
    label_viz = np.zeros((label.shape[0],label.shape[1],3), dtype=np.uint8)
    uids = np.unique(label)
    for uid in uids:
        label_viz[label==uid] = colormap[uid]

    # Convert to PIL image
    label_viz = PIL.Image.fromarray(label_viz)

    # Optionally save image
    if saveto is not None:
        # Create necessary file structure
        pardir = os.path.dirname(saveto)
        if pardir.strip() != "": # ensure pardir is not an empty string
            if not os.path.exists(pardir):
                os.makedirs(pardir)
        label_viz.save(saveto, "JPEG")

    return label_viz


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
#                                               VIZ_OVERLAYED_SEGMENTATION_LABEL
# ==============================================================================
def viz_overlayed_segmentation_label(img, label, colormap=None, alpha=0.5, saveto=None):
    """ Given a base image, and the segmentation label image as numpy arrays,
        It overlays the segmentation labels on top of the base image, color
        coded for each separate class.

    Args:
        img:        (np array) numpy array containing base image (uint8 0-255)
        label:      (np array) numpy array containing segmentation labels,
                    with each pixel value representing the class label.
        colormap:   (None or list of 3-tuples) For each class label, specify
                    the RGB values to color code those pixels. Eg: red would
                    be `(255,0,0)`.
                    If `None`, then it supports up to 4 classes in a default
                    colormap:

                        0 = black
                        1 = red
                        2 = green
                        3 = blue

        alpha:      (float) Alpha value for overlayed segmentation labels
        saveto:     (None or str) Optional filepath to save this
                    visualization as a jpeg image.
    Returns:
        (PIL Image) PIL image of the visualization.
    """
    # Load the image
    img = array2pil(img)
    img = img.convert("RGB")

    # Default colormap
    if colormap is None:
        colormap = [[127,127,127],[255,0,0],[0,255,0],[0,0,255]]
    label = viz_segmentation_label(label, colormap=colormap)

    # Overlay the input image with the label
    overlay = PIL.ImageChops.blend(img, label, alpha=alpha)
    # overlay = PIL.ImageChops.add(img, label, scale=1.0)
    # overlay = PIL.ImageChops.screen(img, label)

    # Optionally save image
    if saveto is not None:
        # Create necessary file structure
        pardir = os.path.dirname(saveto)
        if pardir.strip() != "": # ensure pardir is not an empty string
            if not os.path.exists(pardir):
                os.makedirs(pardir)
        overlay.save(saveto, "JPEG")

    return overlay
