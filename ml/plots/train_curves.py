# ==============================================================================
#                                                                   TRAIN_CURVES
# ==============================================================================
import matplotlib.pyplot as plt
def train_curves(train, valid, saveto=None, title="Accuracy over time", ylab="accuracy", legend_pos="lower right"):
    """ Plots the training curves. If `saveto` is specified, it saves the
        the plot image to a file instead of showing it. 
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.suptitle(title, fontsize=15)
    ax.plot(train, color="#FF4F40",  label="train")
    ax.plot(valid, color="#307EC7",  label="valid")
    ax.set_xlabel("epoch")
    ax.set_ylabel(ylab)

    # Grid lines
    ax.grid(True)
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='#888888', linestyle='-')
    plt.grid(b=True, which='minor', color='#AAAAAA', linestyle='-', alpha=0.2)

    # Legend
    ax.legend(loc=legend_pos, title="", frameon=False,  fontsize=8)

    # Save or show
    if saveto is None:
        plt.show()
    else:
        fig.savefig(saveto)
        plt.close()
