# ==============================================================================
#                                                                   MPL_SHOW_IMG
# ==============================================================================
import matplotlib.pyplot as plt
def mpl_show_img(a, figsize=(15,10)):
    """Given a numpy array representing an image, view it (using matplotlib)"""
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    plt.imshow(a,  cmap="gray")     # Can actually render RGB with "gray"
    ax.grid(False)                     # Remove gridline
    ax.get_yaxis().set_visible(False)  # Remove axis ticks
    ax.get_xaxis().set_visible(False)  # Remove axis ticks
    plt.show()


# ==============================================================================
#                                                                       SHOW_IMG
# ==============================================================================
import PIL
def show_img(a):
    """Given a numpy array representing an image, view it (using PIL)"""
    img = PIL.Image.fromarray(a)
    img.show()
