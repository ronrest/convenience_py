# ==============================================================================
#                                                         RESIZE_BATCH_OF_IMAGES
# ==============================================================================
import scipy.misc
def resize_batch_of_images(x, size=[32, 32], resample="bicubic"):
    """ Given an array that is a batch of images, it resizes the
        images to the desired size [width, height]. You can set
        the resampling interpolation method as one of:

        ‘nearest’, ‘lanczos’, ‘bilinear’, ‘bicubic’ or ‘cubic’
    """
    width, height = size
    n_batch, _, _, channels = x.shape
    new_batch = np.zeros([n_batch, height, width, channels], dtype=np.uint8)
    for i, img in enumerate(x):
        new_batch[i] = scipy.misc.imresize(img, (height,width), interp=resample)
    return new_batch
