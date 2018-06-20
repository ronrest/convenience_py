import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np
import pandas as pd
def setgrid(ax, major=True, minor=False):
    """ Given an axis object, it sets the grids on """
    if major or minor:
        ax.grid(True)

    if major:
        ax.grid(b=True, which='major', color='#999999', linestyle='-', linewidth=1)

    if minor:
        ax.minorticks_on()
        ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.7, linewidth=0.5)


