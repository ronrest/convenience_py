from matplotlib import pyplot as plt

__author__ = 'ronny'

def array2image(x):
    plt.figure()
    plt.imshow(x, cmap="gray")

    plt.show()


