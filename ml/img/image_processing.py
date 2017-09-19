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


def random_crop(im, min_scale=0.5, preserve_size=False, resample=PIL.Image.NEAREST):
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


