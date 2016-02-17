from scipy import ndimage

def image2array(f):
    return ndimage.imread(f).astype(float)

