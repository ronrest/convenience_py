import matplotlib.pyplot as plt
# %matplotlib inline

def plot_history(history, metrics=["loss", "acc"], slice=None, use_valid=True, savedir=None, show=True):
    """ Given a training history from a keras model, it plots the learning
        curves for the given evaluation `metrics`.
    Args:
        history:    (dict) a keras training history dictionary that is returned
                    by model.fit()
        slice:      (2-tuple or None) Only show a slice of the learning curves
                    between [lower_epoch, upper_epoch]
                    - Note, it is inclusive and zero indexed.
                    - If `None`, then shows plot for all epochs.
        metrics:    (list of str) The metric names you want to use from the
                    history dictionary, eg default is ["loss", "acc"]
        use_valid:  (bool) Should it plot the validation versions of the metric
                    alongside the training metric? (default=True)
        savedir:    (None, or str) If not `None`, then it saves the plots as
                    images in this given directory path, and filenames will be
                    `<metric_name>.jpg`, eg, `acc.jpg`
        show:       (bool)(default=True) Should it show the plots on screen?
    """
    titles = {"acc": "Accuracy", "loss": "Loss"}

    # Range of epochs to use
    n_epochs=len(history.history[metrics[0]])
    if slice is None:
        slice = (0, n_epochs-1)
    lower, upper = slice[0], min(slice[1], n_epochs-1)

    for metric in metrics:
        fig, ax = plt.subplots(figsize=(11, 6))
        fig.suptitle(titles.get(metric, metric.title()))
        x = np.arange(lower, upper+1)
        ax.plot(x, history.history[metric][lower:upper+1], linewidth=2.0, color='red', linestyle='-', alpha=0.9, label="train")
        if use_valid:
            ax.plot(x, history.history["val_"+metric][lower:upper+1], linewidth=2.0, color='blue', linestyle='-', alpha=0.9, label="valid")
        ax.legend(loc="lower right", frameon=False)
        if savedir is not None:
            filepath = os.path.join(savedir, metric+".jpg")
            fig.savefig(filepath)
        if show:
            fig.show()
