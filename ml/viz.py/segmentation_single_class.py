"""
Useful functions for the image segmentation task, where there is only a single
class to be labelled. 
"""
__author__ = "Ronny Restrepo"
__copyright__ = "Copyright 2017, Ronny Restrepo"
__credits__ = ["Ronny Restrepo"]
__license__ = "Apache License"
__version__ = "2.0"


# ==============================================================================
#                                                                OVERLAYED_LABEL
# ==============================================================================
import PIL
import numpy as np
def overlayed_label(X, Y):
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


# ==============================================================================
#                                                 OVERLAYED_LABEL_AND_PREDICTION
# ==============================================================================
import PIL
from PIL import Image, ImageChops
from data import maybe_make_pardir
import numpy as np
# Depends on: maybe_make_pardir
def overlayed_label_and_prediction(img, label, pred, saveto=None):
    """ For segmentation task with a single label (label 1 in a flat 2D image).
        Given an input image, the ground truth labels for the pixels, and
        the predictions, It returns an image that overlays the ground
        truth and predictions on top of the original image color coded as:

        blue    = ground truth label
        red     = prediction
        magenta = where ground truth overlaps with prediction

    Args:
        img:    (numpy array) of shape [height, width, 3] of int vals 0-255
        label:  (numpy array) of shape [height, width] of int vals 0-n_classes
        pred:   (numpy array) of shape [height, width] of int vals 0-n_classes

    Returns: (PIL image)
    """
    # pred = np.argmax(pred, axis=2)          # get the most likely class id for each pixel
    assert 2 == label.ndim == pred.ndim, \
        "Label and Prediction MUST be of shape 2D arrays with no color channel or batch axis"
    assert (img.ndim == 3) and (img.shape[-1] == 3), \
        "Input image should be of shape [n_rows, n_cols, 3]"
    assert img.shape[:2] == pred.shape == label.shape, \
        "Image height and width for img, label, and pred must all match up"

    # Convert chanel axis to one hot encodings (max of three classes for 3 chanels)
    pred = np.eye(3, dtype=np.uint8)[pred]
    label = np.eye(3, dtype=np.uint)[label]

    # Extract JUST the road class (class 1)
    # Red for prediction, Blue for label
    road = np.zeros_like(pred)
    road[:,:,0] = pred[:,:,1]*255
    road[:,:,2] = label[:,:,1]*255

    # Overlay the input image with the label and prediction
    img = PIL.Image.fromarray(img)
    road = PIL.Image.fromarray(road)
    overlay = PIL.ImageChops.add(img, road, scale=1.5)

    if saveto is not None:
        maybe_make_pardir(saveto)
        overlay.save(saveto, "JPEG")

    return overlay
