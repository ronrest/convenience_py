# ==============================================================================
#                                                            LOAD_IMAGE_AS_ARRAY
# ==============================================================================
import scipy.misc
def load_image_as_array(f, rescale=None):
    """ Given a filepath to an image file, it loads an image as a numpy array.
        Optionally resize the images to [width, height]"""
    img = scipy.misc.imread(f)
    if rescale:
        width, height = rescale
        img = scipy.misc.imresize(img, (height,width))
    return img
