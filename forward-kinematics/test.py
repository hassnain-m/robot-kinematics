import matplotlib.pyplot as plt
import numpy as np

o = [0,0] #orgin
q1 = np.pi/4 #radians
l1 = 5 * np.sqrt(2) #length of first link
a = [np.cos(q1) * l1, np.sin(q1) * l1] #coordinates of first joint


x = [o[0], a[0]]
y = [o[1], a[1]]


plt.plot(x, y, "bo")
plt.plot(x, y, color="black", linewidth=3)


plt.ylim(0, 20)
plt.xlim(-25, 20)
plt.show()