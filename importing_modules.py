from IPython.display import Image
#from IPython.core.display import HTML 
from IPython.display import HTML

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the Python Image processing Library
from PIL import Image as PILImage

# Makes it possible to do symbolic maths and use a control system lib
import sympy
sympy.init_printing()

# Let's also ignore some warnings here due to sympy using an old matplotlib function to render Latex equations.
import warnings
warnings.filterwarnings('ignore')

# For animations
from matplotlib import animation, rc

# equivalent to rcParams['animation.html'] = 'html5'
rc('animation', html='html5')

# Enable interactive plot
#%matplotlib notebook

import dyna.core as core
from rotate_image import *


def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)