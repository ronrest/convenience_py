from __future__ import print_function, division
import numpy as np
# ==============================================================================
#                                                                     CW2CORNERS
# ==============================================================================
def cw2corners(boxes):
    """
    Given an array of boxes that are in [x,y,w,h] (center, width) format, it
    returns the boxes in [x1,y1,x2,y2] (corners) format.

    It works for both boxes represented as normalized floats between 0-1, and
    absolute integer values, SO LONG as the integer representation is stored
    in an array that has dtype of integer.
    """
    assert boxes.ndim <= 2, "boxes is wrong number of dimensions, should be 2d array"
    if boxes.ndim == 1:
        boxes = np.expand_dims(boxes, axis=0)
    assert boxes.shape[1] == 4, "Boxes must be shape [n_boxes, 4]"

    w2 = boxes[:, 2]/2
    h2 = boxes[:, 3]/2
    out = np.zeros_like(boxes)
    out[:,0] = boxes[:,0]-w2 # x1
    out[:,1] = boxes[:,1]-h2 # y1
    out[:,2] = out[:,0]+boxes[:,2] # x2
    out[:,3] = out[:,1]+boxes[:,3] # y2

    return out

