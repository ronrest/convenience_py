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


################################################################################
#                                   NETWORKS
################################################################################
class BasicNet(nn.Module):
    def __init__(self, img_shape, n_classes):
        """
        img_shape: (3-tuple) (height, width, n_channels)
        """
        super(BasicNet, self).__init__()
        # SETTINGS
        conv_activation = nn.ReLU
        fc_activation = nn.ReLU
        conv_dropout=0.3
        fc_dropout = 0.5
        final_conv_filters = 32

        n_downsamples = 2
        divisor = (2**n_downsamples)
        H, W, C = img_shape
        n_flattened= (W//divisor) * (H//divisor) * final_conv_filters

        # CONV LAYERS
        trunk = nn.Sequential()
        trunk.add_module("conv1", conv(3, 16, k=3, s=1, d=1, bn=True, bias=False, dropout=conv_dropout, activation=conv_activation))
        trunk.add_module("mp1", nn.MaxPool2d(kernel_size=2, stride=2, padding=0))
        trunk.add_module("conv2", conv(16, final_conv_filters, k=3, s=1, d=1, bn=True, bias=False, dropout=conv_dropout, activation=conv_activation))
        trunk.add_module("mp2", nn.MaxPool2d(kernel_size=2, stride=2, padding=0))
        self.trunk = trunk

        # FC LAYERS
        head = nn.Sequential()
        # head.add_module("flatten", Flatten())
        head.add_module("fc1", fc(n_flattened, 128, bn=True, bias=False, dropout=fc_dropout, activation=fc_activation))
        head.add_module("fc2", fc(128, n_classes, bn=False, bias=True, dropout=None, activation=None))
        self.head = head

    def forward(self, x):
        x = self.trunk(x)
        x = flatten(x)
        x = self.head(x)
        return x
