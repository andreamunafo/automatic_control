# AUTOGENERATED! DO NOT EDIT! File to edit: 99_refs.ipynb (unless otherwise specified).

__all__ = []

# Cell
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-white')

# Cell
def _subfigure(rows, cols):
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    axs = []
    for i in range(1, rows*cols+1):
        axs.append(fig.add_subplot(rows, cols, i))

    return fig, axs
        #ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')