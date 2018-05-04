import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)

s = 1 + np.sin(2 * np.pi * t)

d1 = np.arange(0,10,1)
d2 = np.arange(0,20,2)

# fig, ax = plt.subplots() is same as blow
fig = plt.figure()
ax = fig.add_subplot(111)


ax.grid()
ax.plot(t,s,'rx',d1,d2,'g--')
plt.show()
