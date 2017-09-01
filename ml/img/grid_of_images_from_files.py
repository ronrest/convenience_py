import Image
import numpy as np

# ==============================================================================
#                                                                 GRID_OF_IMAGES
# ==============================================================================
def grid_of_images_from_files(files, dims=(50,50), mode="RGB", save=None):
    """
    Takes a 2D array  of filepaths to images, and returns a single big image
    with each of those individual images appearing in a grid.

    eg, given the following array:
            [["car.png", "flower.png", "ship.png"],
             ["duck.png" , "horse.png", "house.png"]]

    This will generate an image composed of a 2x3 grid of image cells.

    You can specify how big you want the small image cells to be.

    :param files: {2D array-like of strings}
        A 2D array of filepaths to image files.
    :param dims: {tuple of ints} {default = (50.50)}
        (width, height) that you want each small image cell to be.

    :param mode:{string} {default = "RGB"}
        Color mode for the output image.
        "RGB"  = (3x8-bits per pixel)
        "RGBA" = (4x8-bits per pixel with transparency)
        "GREY" = greyscale (8-bits per pixel, black and white)
        "BW"   = pure black or white pixels (1-bit per pixel, black and white)

    :param save: {None or string}{default=None}
        If None, then it will simply return the image

        If it is a string, then this string should be the filename to save the
        image as.

    :return: {image object, or None}
        depending on the option you used for `save`.
    """
    # ==========================================================================
    files = np.array(files) # convert files to a numpy array

    # map for color modes accepted by this funciton to the modes accepted by
    # Image.new()
    mode_map = {
        "RGB"  : "RGB",
        "RGBA" : "RGBA",
        "GREY" : "L",
        "BW"   : "1"
    }
    # Dimensions
    width = dims[0]
    height = dims[1]
    rows = files.shape[0]
    cols = files.shape[1]

    # Initialise blank image to be used for grid of images
    grid_image = Image.new(mode_map[mode], (width*cols, height*rows))

    # For each image in the files array, add it to the grid of images.
    for i, pos_x in enumerate(xrange(0,width*cols, width)):
        for j, pos_y in enumerate(xrange(0, height * rows, height)):
            cell_image = Image.open(files[j,i])
            cell_image.thumbnail((width, height))
            grid_image.paste(cell_image, (pos_x, pos_y))

    # ---------------------------------------------------
    #                                   Return or Save
    # ---------------------------------------------------
    if save is None:
        return grid_image
    else:
        grid_image.save(save)
