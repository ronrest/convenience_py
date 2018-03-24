# %load_ext autoreload
# %autoreload 2
import torch
from torch import nn
from torch.autograd import Variable

def accuracy(preds, labels):
    return (preds==labels).mean()

def n_correct(preds, labels):
    return (preds==labels).sum()


class ImageClassifier(object):
    def __init__(self, net, n_classes):
        """
        Args:
            net:    A pytorch network module that will computer a forward pass
            n_classes: number of output classes.
        """
        self.history = []
        self.n_classes = n_classes
        self.net = net

        # LOSS FUNCTION
        if n_classes <= 2:
            # Binary classification
            self.loss_func = torch.nn.BCEWithLogitsLoss(weight=None)
        else:
            # multiclass classification
            self.loss_func = torch.nn.CrossEntropyLoss(weight=None) # on logits
            #self.loss_func = torch.nn.NLLLoss(weight=None) #on LogSoftmax() outputs

        # OPTIMIZER
        self.optimizer = None

