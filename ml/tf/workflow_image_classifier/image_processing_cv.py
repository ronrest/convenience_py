import cv2
import numpy as np
randint = np.random.randint

__author__ = "Ronny Restrepo"
__copyright__ = "Copyright 2018, Ronny Restrepo"
__credits__ = ["Ronny Restrepo"]
__license__ = "Apache License"
__version__ = "2.0"

# import PIL
# from PIL import Image
# x = cv2.imread("/home/ronny/cat.jpg")
# x = cv2.resize(x, (100,100))
# y = cv2.warpAffine(x, m, x.shape[:2])
# PIL.Image.fromarray(y).show()
# PIL.Image.fromarray(y).show()

# ==============================================================================
#                                                                  BATCH_PROCESS
# ==============================================================================
def batch_process(X, shape=None, mode=None):
    # TODO: currently does nothing
    return X


# ==============================================================================
#                                                                    RANDOM_CROP
# ==============================================================================
def random_crop(im, min_scale=0.5, max_scale=1.0, preserve_size=False):
    """
    Args:
        im:          (numpy array) input image
        min_scale:   (float) minimum ratio along each dimension to crop from.
        max_scale:   (float) maximum ratio along each dimension to crop from.
        preserve_size: (bool) Should it resize back to original dims?

    Returns:
        (numpy array) randomly cropped image.
    """
    assert (min_scale < max_scale), "min_scale MUST be smaller than max_scale"
    width, height = im.shape[:2]
    crop_width = np.random.randint(width*min_scale, width*max_scale)
    crop_height = np.random.randint(height*min_scale, height*max_scale)
    x_offset = np.random.randint(0, width - crop_width + 1)
    y_offset = np.random.randint(0, height - crop_height + 1)

    im2 = im[y_offset:y_offset+crop_height,
             x_offset:x_offset+crop_width]
    if preserve_size:
        im2 = cv2.resize(im2, tuple(im.shape[:2]))
    return im2
