import Image
import numpy as np

def grid_of_images(files, dims=(50,50), mode="RGB", save=None):
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

