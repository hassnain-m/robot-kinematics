import matplotlib.pyplot as plt
import numpy as np

origin = [0,0]
q1 = np.pi/4 #radians
l1 = 5 * np.sqrt(2)

a = [np.cos(q1) * l1, np.sin(q1) * l1]

plt.plot(a[0], a[1], "bo")
plt.plot(origin[0], origin[1], "bo")

plt.show()