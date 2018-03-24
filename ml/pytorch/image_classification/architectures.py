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


