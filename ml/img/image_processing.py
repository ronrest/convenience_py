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


# ==============================================================================
#                                                                    SHIFT_IMAGE
# ==============================================================================
def shift_image(im, shift):
    """ Shifts an image.

    Args:
        im
        shift:  [x,y]
    """
    return ImageChops.offset(im, xoffset=shift[0], yoffset=shift[1])


# ==============================================================================
#                                                              RANDOM_BRIGHTNESS
# ==============================================================================
def random_brightness(im, sd=0.5, min=0, max=20):
    """Creates a new image which randomly adjusts the brightness of `im` by
       randomly sampling a brightness value centered at 1, with a standard
       deviation of `sd` from a normal distribution. Clips values to a
       desired min and max range.

    Args:
        im:   PIL image
        sd:   (float) Standard deviation used for sampling brightness value.
        min:  (int or float) Clip contrast value to be no lower than this.
        max:  (int or float) Clip contrast value to be no higher than this.


    Returns:
        PIL image with brightness randomly adjusted.
    """
    brightness = np.clip(np.random.normal(loc=1, scale=sd), min, max)
    enhancer = ImageEnhance.Brightness(im)
    return enhancer.enhance(brightness)


# ==============================================================================
#                                                                RANDOM_CONTRAST
# ==============================================================================
def random_contrast(im, sd=0.5, min=0, max=10):
    """Creates a new image which randomly adjusts the contrast of `im` by
       randomly sampling a contrast value centered at 1, with a standard
       deviation of `sd` from a normal distribution. Clips values to a
       desired min and max range.

    Args:
        im:   PIL image
        sd:   (float) Standard deviation used for sampling contrast value.
        min:  (int or float) Clip contrast value to be no lower than this.
        max:  (int or float) Clip contrast value to be no higher than this.

    Returns:
        PIL image with contrast randomly adjusted.
    """
    contrast = np.clip(np.random.normal(loc=1, scale=sd), min, max)
    enhancer = ImageEnhance.Contrast(im)
    return enhancer.enhance(contrast)


# ==============================================================================
#                                                                    RANDOM_BLUR
# ==============================================================================
def random_blur(im, min=0, max=5):
    """ Creates a new image which applies a random amount of Gaussian Blur, with
        a blur radius that is randomly chosen to be in the range [min, max]
        inclusive.

    Args:
        im:   PIL image
        min:  (int) Min amount of blur desired.
        max:  (int) Max amount of blur desired.


    Returns:
        PIL image with random amount of blur applied.
    """
    blur_radius = randint(min, max+1)
    if blur_radius == 0:
        return im
    else:
        return im.filter(ImageFilter.GaussianBlur(radius=blur_radius))


# ==============================================================================
#                                                                   RANDOM_NOISE
# ==============================================================================
def random_noise(im, sd=5):
    """Creates a new image which has random noise.
       The intensity of the noise is determined by first randomly choosing the
       standard deviation of the noise as a value between 0 to `sd`.
       This value is then used as the standard deviation for randomly sampling
       individual pixel noise from a normal distribution.
       This random noise is added to the original image pixel values, and
       clipped to keep all values between 0-255.

    Args:
        im:   PIL image
        sd:   (int) Max Standard Deviation to select from.

    Returns:
        PIL image with random noise added.
    """
    mode = im.mode
    noise_sd = np.random.randint(0, sd)
    if noise_sd > 0:
        noise = np.random.normal(loc=0, scale=noise_sd, size=np.shape(im))
        im2 = np.clip(im + noise, 0, 255).astype(np.uint8)
        return array2pil(im2, mode=mode)
    else:
        return im


# ==============================================================================
#                                                                RANDOM_ROTATION
# ==============================================================================
def random_rotation(im, max=10, expand=True):
    """ Creates a new image which is rotated by a random amount between
        [-max, +max] inclusive.

    Args:
        im:     PIL image
        max:    (int) Max angle (in either direction).
        expand: (bool) expand image to prevent rotated edges being visible.

    Returns:
        PIL image with random rotation applied.
    """
    angle = randint(-max, max+1)
    if angle == 0:
        return im
    else:
        return im.rotate(angle, resample=Image.BILINEAR, expand=expand)


# ==============================================================================
#                                   RANDOM_TRANSFORMATIONS_FOR_SEGMENTATION_DATA
# ==============================================================================
def random_transformations_for_segmentation_data(X, Y, brightness=True, contrast=True, blur=3, crop=0.5, noise=10):
    """ Takes a batch of input images `X`, segmentation labels `Y` as arrays,
        and does random image transormations on them.

        Ensures that any tansformations that shift or scale the input images
        also have the same transormations applied to the label images.

    NOTE:  Assumes the pixels for input images are in the range of 0-255.

    Args:
        X:          (numpy array) batch of imput images
        Y:          (numpy array) batch of segmentation labels
        brightness: (bool)(default=True)
                    Apply random brightness?
        contrast:   (bool)(default=True)
                    Apply random contrast?
        blur:       (int or None)(default=3)
                    Amount of gaussian blur to apply (in pixels).
        crop:       (float or None)(default=0.5)
                    Smallest crop to take as a ratio of the dimensions of the
                    original image.
                    Eg, `crop=0.5` could crop a region of the image ranging
                    anywhere from 50x50 - 100x100 for an input image of 100x100.
        noise:      (int or None)(default=10)
                    Standard deviation (as a pixel intensity value) to use
                    for random normal noise to apply to each pixel.
                    (gets clipped to keep pixel values between 0-255)
    """
    images = np.zeros_like(X)
    labels = np.zeros_like(Y)
    n_images = len(images)
    for i in range(n_images):
        image = array2pil(X[i], mode="RGB")
        label = array2pil(Y[i], mode="L")

        if brightness:
            image = random_brightness(image, sd=0.5, min=0.2, max=4)
        if contrast:
            image = random_contrast(image, sd=0.5, min=0.2, max=5)
        if crop is not None:
            min_scale = crop
            width, height = np.array(np.shape(image)[:2])
            crop_width = np.random.randint(width*min_scale, width)
            crop_height = np.random.randint(height*min_scale, height)
            x_offset = np.random.randint(0, width - crop_width + 1)
            y_offset = np.random.randint(0, height - crop_height + 1)
            image = crop_and_preserve_size(image, crop_dims=[crop_width, crop_height], offset=[x_offset, y_offset])
            label = crop_and_preserve_size(label, crop_dims=[crop_width, crop_height], offset=[x_offset, y_offset])
        if blur is not None:
            image = random_blur(image, 0, blur)

        if noise is not None:
            image = random_noise(image, sd=noise)

        # Put into array
        images[i] = pil2array(image)
        labels[i] = pil2array(label)
    return images, labels
