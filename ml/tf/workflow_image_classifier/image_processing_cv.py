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
#                                                                RANDOM_ROTATION
# ==============================================================================
def random_rotation(im, max=10):
    """ Creates a new image which is rotated by a random amount between
        [-max, +max] inclusive.

    Args:
        im:              (numpy array) Input Image
        max:             (int) Max angle (in degrees in either direction).
    Returns:
        (numpy array) Image with random rotation applied.

    NOTE:
        The Current implementation clips the corners that lie outside of
        the original image container dimensions when rotated.
    """
    # TODO: give option to preserve corners by calculating the `scale` factor
    #       that would be needed to preserve them.
    angle = randint(-max, max+1)
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


# ==============================================================================
#                                                         RANDOM_TRANSFORMATIONS
# ==============================================================================
def random_transformations(
    X,
    shadow=(0.6, 0.9),
    shadow_file="shadow_pattern.jpg",
    shadow_crop_range=(0.02, 0.5),
    rotate=180,
    crop=0.5,
    lr_flip=True,
    tb_flip=True,
    brightness=(0.5, 0.4, 4),
    contrast=(0.5, 0.3, 5),
    blur=3,
    noise=10
    ):
    """ Takes a batch of input images `X` as a numpy array, and does random
        image transormations on them.

        NOTE:  Assumes the pixels for input images are in the range of 0-255.

    Args:
        X:                  (numpy array) batch of imput images
        Y:                  (numpy array) batch of segmentation labels
        shadow:             (tuple of two floats) (min, max) shadow intensity
        shadow_file:        (str) Path fo image file containing shadow pattern
        shadow_crop_range:  (tuple of two floats) min and max proportion of
                            shadow image to take crop from.
        shadow_crop_range:  ()(default=(0.02, 0.25))
        rotate:             (int)(default=180)
                            Max angle to rotate in each direction
        crop:               (float)(default=0.5)
        lr_flip:            (bool)(default=True)
        tb_flip:            (bool)(default=True)
        brightness:         ()(default=) (std, min, max)
        contrast:           ()(default=) (std, min, max)
        blur:               ()(default=3)
        noise:              ()(default=10)

    NOTE:

    """
    # TODO: Random warping
    # TODO: shadow
    # TODO: brightness, contrast, blur, noise
    img_shape = X[0].shape[:2]
    images = np.zeros_like(X)
    n_images = len(images)

    # if shadow is not None:
    #     assert shadow[0] < shadow[1], "shadow max should be greater than shadow min"
    #     shadow_image = PIL.Image.open(shadow_file)
    #     # Ensure shadow is same color mode as input images
    #     shadow_image = shadow_image.convert(get_array_color_mode(X[0]))

    for i in range(n_images):
        image = X[i]
        original_dims = image.shape[:2]

        # if shadow is not None:
        #     image = random_shadow(image, shadow=shadow_image, intensity=shadow, crop_range=shadow_crop_range)

        if rotate:
            # image = random_90_rotation(image)
            image = random_rotation(image, max=rotate)

        if crop is not None:
            image = random_crop(image, min_scale=crop, max_scale=1.0, preserve_size=True)

        # Scale back after crop and rotate are done
        if rotate or crop:
            image = cv2.resize(image, tuple(original_dims))

        if lr_flip:
            image = random_lr_flip(image)

        if tb_flip:
            image=  random_tb_flip(image)

        # if brightness is not None:
        #     image = random_brightness(image, sd=brightness[0], min=brightness[1], max=brightness[2])
        # if contrast is not None:
        #     image = random_contrast(image, sd=contrast[0], min=contrast[1], max=contrast[2])
        # if blur is not None:
        #     image = random_blur(image, 0, blur)

        # if noise:
        #     image = random_noise(image, sd=noise)

        # Put into array
        images[i] = image
    return images


