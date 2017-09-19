import PIL
from PIL import ImageEnhance, Image, ImageFilter, ImageChops
import numpy as np
randint = np.random.randint


# ==============================================================================
#                                                                      PIL2ARRAY
# ==============================================================================
def pil2array(im):
    """ Given a PIL image it returns a numpy array representation """
    return np.asarray(im, dtype=np.uint8)


# ==============================================================================
#                                                                      ARRAY2PIL
# ==============================================================================
def array2pil(a, mode="RGB"):
    """Given a numpy array containing image information returns a PIL image"""
    if mode.lower() in ["grey", "gray", "l"]:
        mode="L"
    return Image.fromarray(a, mode=mode)


# ==============================================================================
#                                                                    RANDOM_CROP
# ==============================================================================
def random_crop(im, min_scale=0.5, preserve_size=False, resample=PIL.Image.NEAREST):
    """
    Args:
        im:             (PIL image)
        min_scale:      (float) minimum ratio along each dimension to crop from.
        preserve_size:  (bool) Should it resize to original image dimensions?
        resample:       Resampling method during rescale.

    Returns:
        PIL image randomly cropped from `im`.
    """
    if min_scale == 0:
        return im
    else:
        width, height = np.array(np.shape(im)[:2])
        crop_width = np.random.randint(width*min_scale, width)
        crop_height = np.random.randint(height*min_scale, height)
        x_offset = np.random.randint(0, width - crop_width + 1)
        y_offset = np.random.randint(0, height - crop_height + 1)
        im2 = im.crop((x_offset, y_offset,
                       x_offset + crop_width,
                       y_offset + crop_height))
        if preserve_size:
            im2 = im2.resize(im.size, resample=resample)
        return im2


# ==============================================================================
#                                                         CROP_AND_PRESERVE_SIZE
# ==============================================================================
def crop_and_preserve_size(im, crop_dims, offset, resample=PIL.Image.NEAREST):
    """ Given a PIL image, the dimensions of the crop, and the offset of
        the crop, it crops the image, and resizes it back to the original
        dimensions.

    Args:
        im:         (PIL image)
        crop_dims:  Dimensions of the crop region [width, height]
        offset:     Position of the crop box from Top Left corner [x, y]
        resample:   resamplimg method
    """
    crop_width, crop_height = crop_dims
    x_offset, y_offset = offset
    im2 = im.crop((x_offset, y_offset,
                   x_offset + crop_width,
                   y_offset + crop_height))
    im2 = im2.resize(im.size, resample=resample)
    return im2


# ==============================================================================
#                                                                   RANDOM_SHIFT
# ==============================================================================
def random_shift(im, max=(5,5)):
    """ Randomly shifts an image.

    Args:
        im: (pil image)
        max: (tuple of two ints) max amount in each x y direction.
    """
    x_offset = np.random.randint(0, max[0])
    y_offset = np.random.randint(0, max[1])
    return ImageChops.offset(im, xoffset=x_offset, yoffset=y_offset)


