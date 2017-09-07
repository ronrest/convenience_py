

# ==============================================================================
#                                                            LOAD_IMAGE_AS_ARRAY
# ==============================================================================
from scipy import misc
def load_image_as_array(f):
    """ Given a filepath to an image file, it loads an image as a numpy array"""
    return scipy.misc.imread(f)
