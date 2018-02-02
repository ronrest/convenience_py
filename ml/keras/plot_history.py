import matplotlib.pyplot as plt
# %matplotlib inline

def plot_history(history, metrics=["loss", "acc"], use_valid=True, savedir=None, show=True):
    titles = {"acc": "Accuracy", "loss": "Loss"}
    for metric in metrics:
        fig, ax = plt.subplots(figsize=(11, 6))
        fig.suptitle(titles.get(metric, metric.title()))
        ax.plot(history.history[metric], linewidth=2.0, color='red', linestyle='-', alpha=0.9, label="train")
        if use_valid:
            ax.plot(history.history["val_"+metric], linewidth=2.0, color='blue', linestyle='-', alpha=0.9, label="valid")
        ax.legend(loc="lower right", frameon=False)
        if savedir is not None:
            filepath = os.path.join(savedir, metric+".jpg")
            fig.savefig(filepath)
        if show:
            fig.show()
