import numpy as np


# ==============================================================================
#                                                              PIXELS_WITH_VALUE
# ==============================================================================
def pixels_with_value(img, val):
    """ Given an image as a numpy array, and a value representing the
        pixel values, eg [128,255,190] in an RGB image, then it returns
        a 2D boolean array with a True for every pixel position that has
        that value.
    """
    return np.all(img==np.array(val), axis=2)


# ==============================================================================
#                                                                   RGB2SEGLABEL
# ==============================================================================
def rgb2seglabel(img, colormap, channels_axis=False):
    """ Given an RGB image stored as a numpy array, and a colormap that
        maps from label id to an RGB color for that label, it returns a
        new numpy array with color chanel size of 1 where the pixel
        intensity values represent the class label id.

    Args:
        img:            (np array)
        colormap:       (list) list of pixel values for each class label id
        channels_axis:  (bool)(default=False) Should it return an array with a
                        third (color channels) axis of size 1?
    """
    height, width, _ = img.shape
    if channels_axis:
        label = np.zeros([height, width,1], dtype=np.uint8)
    else:
        label = np.zeros([height, width], dtype=np.uint8)
    for id in range(len(colormap)):
        label[np.all(img==np.array(idcolormap[id]), axis=2)] = id
    return label


# ==============================================================================
#                                                       LOAD_IMAGE_AND_SEGLABELS
# ==============================================================================
def load_image_and_seglabels(input_files, label_files, colormap, shape=(32,32), n_channels=3, label_chanel_axis=False):
    """ Given a list of input image file paths and corresponding segmentation
        label image files (with different RGB values representing different
        classes), and a colormap list, it:

        - loads up the images
        - resizes them to a desired shape
        - converts segmentation labels to single color channel image with
          integer value of pixel representing the class id.

    Args:
        input_files:        (list of str) file paths for input images
        label_files:        (list of str) file paths for label images
        colormap:           (list or None) A list where each index represents the
                            color value for the corresponding class id.
                            Eg: for RGB labels, to map class_0 to black and
                            class_1 to red:
                                [(0,0,0), (255,0,0)]
                            Set to None if images are already encoded as
                            greyscale where the integer value represents the
                            class id.
        shape:              (2-tuple of ints) (width,height) to reshape images
        n_channels:         (int) Number of chanels for input images
        label_chanel_axis:  (bool)(default=False) Use color chanel axis for
                            array of label images?
    """
    # Dummy proofing
    assert n_channels in {1,3}, "Incorrect value for n_channels. Must be 1 or 3. Got {}".format(n_channels)

    # Image dimensions
    width, height = shape
    n_samples = len(label_files)

    # Initialize input and label batch arrays
    X = np.zeros([n_samples, height, width, n_channels], dtype=np.uint8)
    if label_chanel_axis:
        Y = np.zeros([n_samples, height, width, 1], dtype=np.uint8)
    else:
        Y = np.zeros([n_samples, height, width], dtype=np.uint8)

    for i in range(n_samples):
        # Get filenames of input and label
        img_file = input_files[i]
        label_file = label_files[i]

        # Resize input and label images
        img = PIL.Image.open(img_file).resize(shape, resample=PIL.Image.CUBIC)
        label_img = PIL.Image.open(label_file).resize(shape, resample=PIL.Image.NEAREST)

        # Convert back to numpy arrays
        img = np.asarray(img, dtype=np.uint8)
        label_img = np.asarray(label_img, dtype=np.uint8)

        # Convert label image from RGB to single value int class labels
        if colormap is not None:
            label_img = rgb2seglabel(label_img, colormap=colormap, channels_axis=label_chanel_axis)

        # Add processed images to batch arrays
        X[i] = img
        Y[i] = label_img

    return X, Y
