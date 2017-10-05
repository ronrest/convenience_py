import PIL
import PIL.Image
import numpy as np
import os
def viz_segmentation_label(label, color_mapper=None, saveto=None):
    if color_mapper is None:
        # Default color mapper
        color_mapper = [[0,0,0],
                        [48,126,199],
                        [115,173,33],
                        [255,79,64],
                        ]
    # Map each pixel label to a color
    label_viz = np.zeros((label.shape[0],label.shape[1],3), dtype=np.uint8)
    uids = np.unique(label)
    for uid in uids:
        label_viz[label==uid] = color_mapper[uid]

    # Convert to PIL image
    label_viz = PIL.Image.fromarray(label_viz)

    if saveto is not None:
        # Create necessary file structure
        pardir = os.path.dirname(saveto)
        if pardir.strip() != "": # ensure pardir is not an empty string
            if not os.path.exists(pardir):
                os.makedirs(pardir)
        label_viz.save(saveto, "JPEG")

    return label_viz
