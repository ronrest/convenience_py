# ==============================================================================
#                                                            LOAD_IMAGE_AS_ARRAY
# ==============================================================================
# USING SCIPY (with i think PIL on the backend)
import scipy.misc
def load_image_as_array(f, rescale=None):
    """ Given a filepath to an image file, it loads an image as a numpy array.
        Optionally resize the images to [width, height]"""
    img = scipy.misc.imread(f)
    if rescale:
        width, height = rescale
        img = scipy.misc.imresize(img, (height,width))
    return img


# USING OPEN CV
def load_image_as_array(f, rescale=None):
    # TODO: Check the order of the dimensions for resizing in open cv
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert to RGB
    if rescale:
        img = cv2.resize(img, rescale)
    return img


# ==============================================================================
#                                                           LOAD_BATCH_OF_IMAGES
# ==============================================================================
def load_batch_of_images(file_list, img_shape):
    """ Given a list of file images to load, it loads them as an array.
    Args:
        file_list:
        img_shape: (tuple of two ints)(width,height)
    Return:
        Numpy array of shape [n_images, img_shape[1], img_shape[0], n_channels]
    """
    n_channels = 3      # Number of channels to use
    n_samples = len(file_list)
    width, height = img_shape
    images = np.zeros([n_samples, height, width, n_channels], dtype=np.uint8)

    # Populate each image at a time into the dataset
    for i, img_file in enumerate(file_list):
        img = scipy.misc.imread(img_file)

        # PROCESS THE IMAGES
        img = scipy.misc.imresize(img, img_shape) # resize

        # Add the processed image to the array
        images[i] = img

    return images
