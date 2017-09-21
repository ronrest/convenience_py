"""
Useful functions for the image segmentation task
"""
__author__ = "Ronny Restrepo"
__copyright__ = "Copyright 2017, Ronny Restrepo"
__credits__ = ["Ronny Restrepo"]
__license__ = "Apache License"
__version__ = "2.0"


# ==============================================================================
#                                          OVERLAYED_SINGLE_CATEGORY_LABEL_IMAGE
# ==============================================================================
import PIL
import numpy as np
def overlayed_single_category_label_image(X, Y):
    """ For the task of classifying a single class.
        Given an image of the scene, and an image of the label,
        where the class of interest is labelled as a 1 on a 2d
        image with no color chanels axis. It returns a PIL image
        of the label overlayed on top of the scene image.

        Images can be either numpy arrays, or PIL image objects.
    """
    # Ensure images correct type
    if type(X) == PIL.Image.Image:
        img = X
    else:
        img = PIL.Image.fromarray(X)
    if type(Y) == PIL.Image.Image:
        Y = np.asarray(Y)

    road = np.zeros_like(X)
    # road[:,:,0] = pred[:,:,1]*255
    road[:,:,2] = Y*255
    road = PIL.Image.fromarray(road)

    # Overlay the input image with the label and prediction
    overlay = PIL.ImageChops.add(img, road, scale=1.5)
    return overlay
