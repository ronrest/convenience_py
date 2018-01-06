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


# ==============================================================================
#                                                         CROP_AND_PRESERVE_SIZE
# ==============================================================================
def crop_and_preserve_size(im, crop_dims, offset):
    """ Given a image, the dimensions of the crop, and the offset of
        the crop, it crops the image, and resizes it back to the original
        dimensions.

    Args:
        im:         (numpy array) Input image
        crop_dims:  Dimensions of the crop region [width, height]
        offset:     Position of the crop box from Top Left corner [x, y]
    Returns:
        (numpy array) cropped image, rescaled to original input image
        dimensions.
    """
    crop_width, crop_height = crop_dims
    x_offset, y_offset = offset
    im2 = im[y_offset:y_offset+crop_height,
             x_offset:x_offset+crop_width]
    im2 = cv2.resize(im2, tuple(im.shape[:2]))
    return im2


# ==============================================================================
#                                                             RANDOM_90_ROTATION
# ==============================================================================
def random_90_rotation(im):
    """ Randomly rotates image in 90 degree increments
        (0, 90, -90, or 180 degrees) """
    angles = [0, 90, -90, 180]
    angle = np.random.choice(angles)

    if angle == 0:
        return im
    else:
        pivot = np.array(im.shape[:2])//2
        m = cv2.getRotationMatrix2D(center=tuple(pivot), angle=-angle, scale=1)
        return cv2.warpAffine(im, m, im.shape[:2])


# ==============================================================================
#                                                                 RANDOM_LR_FLIP
# ==============================================================================
def random_lr_flip(im):
    """ Randomly flips the image left-right with 0.5 probablility """
    if np.random.choice([0,1]) == 1:
        return cv2.flip(im, flipCode=1)
    else:
        return im


# ==============================================================================
#                                                                 RANDOM_TB_FLIP
# ==============================================================================
def random_tb_flip(im):
    """ Randomly flips the image top-bottom with 0.5 probablility """
    if np.random.choice([0,1]) == 1:
        return cv2.flip(im, flipCode=0)
    else:
        return im


# ==============================================================================
#                                                                   RANDOM_SHIFT
# ==============================================================================
def random_shift(im, max=(5,5)):
    """ Randomly shifts an image.

    Args:
        im: (numpy array) Input image
        max: (2-tuple of ints) max amount in each x y direction.
    """
    x_offset = np.random.randint(-max[0], max[0])
    y_offset = np.random.randint(-max[0], max[1])
    m = np.float32([ [1,0,x_offset], [0,1,y_offset]])
    return cv2.warpAffine(im, m, im.shape[:2])


# ==============================================================================
#                                                                    SHIFT_IMAGE
# ==============================================================================
def shift_image(im, shift):
    """ Returns a shifted copy of a PIL image.
    Args:
        im:     (numpy array) Input image
        shift:  (2-tuple of ints) How much to shift along each axis (x, y)
    """
    m = np.float32([ [1,0,shift[0]], [0,1,shift[1]]])
    return cv2.warpAffine(im, m, im.shape[:2])
