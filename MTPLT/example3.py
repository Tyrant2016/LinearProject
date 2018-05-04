import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

dx, dy = 0.05, 0.05
x, y = np.mgrid[slice(1, 5 + dx, dx),
                slice(1, 5 + dy, dy)]
s1,s2=np.mgrid[0:4,0:3]

