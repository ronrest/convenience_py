

# ==============================================================================
#                                                                   SHOW_IMGFILE
# ==============================================================================
from PIL import Image
def show_imgfile(f, size=None):
    """ Given a filepath it opens up the image using PIL. Optionally allows
        you to resize it before viewing.
    """
    img = Image.open(f)
    if size is not None:
         img.resize(size, Image.ANTIALIAS)
    img.show()
