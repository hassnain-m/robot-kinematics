"""
Experiment with Forward Kinematics Here
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


o = [0,0] #orgin
l1 = 5 * np.sqrt(2) #length of first link
q1 = np.pi/4 #radians
a = [np.cos(q1) * l1, np.sin(q1) * l1] #coordinates of first joint
x, y = [o[0], a[0]], [o[1], a[1]]

def update(value):
    rad = float(value) * (np.pi / 180)
    print(rad)
    a = [np.cos(rad) * l1, np.sin(rad) * l1]
    x, y = [o[0], a[0]], [o[1], a[1]]
    line.set_data(x, y)
    figure.canvas.draw_idle()

line = plt.plot(x, y, color="black", linewidth=3)[0]
figure = plt.gcf()

root = tk.Tk()
root.geometry("600x200")
root.title("Forward Kinematics")

h1 = tk.Label(root, text = "q1 angle (degrees)")
slider1 = tk.Scale(root, from_=-360, to_=360, orient="horizontal", length=600, command=update)
slider1.pack()
h1.pack()


h2 = tk.Label(root, text = "q2 angle (degrees)")
slider2 = tk.Scale(root, from_=-360, to_=360, orient="horizontal", length=600)
slider2.pack()
h2.pack()


plt.ylim(0, 20)
plt.xlim(-25, 20)
plt.show()
tk.mainloop()
