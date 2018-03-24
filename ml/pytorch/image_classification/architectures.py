import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

################################################################################
#                                   SUPPORT
################################################################################
class Flatten(nn.Module):
    """ Module to Flatten a layer """
    def forward(self, input):
        return input.view(input.size(0), -1)


def flatten(x):
    return x.view(x.size(0), -1)


################################################################################
#                                   LAYERS
################################################################################
def conv(fin, out, k=3, s=1, d=1, bn=True, bias=False, dropout=None, activation=nn.ReLU):
    """ Convolutional module
        By default uses same padding
        CONV > BatchNorm > Activation > Dropout
    """
    # naive calculation of padding
    p = (k-1)//2

    # Conv
    sq = nn.Sequential()
    sq.add_module("conv", nn.Conv2d(fin, out, k, stride=s, padding=p, dilation=d, bias=bias))

    # Optional components
    if bn:
        sq.add_module("bn", nn.BatchNorm2d(out))
    if activation is not None:
        sq.add_module("activation", activation())
    if dropout is not None:
        sq.add_module("dropout", nn.Dropout2d(p=dropout))
    return sq


def fc(fin, out, bn=True, bias=False, dropout=None, activation=nn.ReLU):
    """ Fully connected module
        FC > BatchNorm > Activation > Dropout
    """
    sq = nn.Sequential()
    sq.add_module("fc", nn.Linear(fin, out, bias=bias))

    if bn is not None:
        sq.add_module("bn", nn.BatchNorm1d(out))
    if activation is not None:
        sq.add_module("activation", activation())
    if dropout is not None:
        sq.add_module("dropout", nn.Dropout(p=dropout))
    return sq


