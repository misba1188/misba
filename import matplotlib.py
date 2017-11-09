import matplotlib.pyplot as plt
import numpy as np
from matplotlib import interactive
interactive(True)

x = np.arange(0,5,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show