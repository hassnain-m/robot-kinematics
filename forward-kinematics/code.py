"""
Experiment with Forward Kinematics Here
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def to_degrees(value):
    return float(value) * 180 / np.pi

def to_radians(value):
    return float(value) * np.pi / 180

#--------Initial Values--------
o = [0,0] #orgin
l1 = 5  #length of first link
l2 = 5 #length of second link
q1 = np.pi/4 #q1 starting angle in radians
q2 = np.pi/12 #q2 starting angle in radians
a = [np.cos(q1) * l1, np.sin(q1) * l1] #coordinates of first joint
b = [a[0]+(np.cos(q2) * l1), a[1]+(np.sin(q2) * l1)] #coordinates of second joint
x1, y1 = [o[0], a[0]], [o[1], a[1]] #line 1 x and y coordintes
x2, y2 = [a[0], b[0]], [a[1], b[1]] #line 2 x and y coordinates


def moveline1(value):
    q1 = to_radians(value)
    #print(rad)
    a = [np.cos(q1) * l1, np.sin(q1) * l1]
    x1, y1 = [o[0], a[0]], [o[1], a[1]]
    b = [a[0] + (np.cos(q2) * l1), a[1] + (np.sin(q2) * l1)]
    x2, y2 = [a[0], b[0]], [a[1], b[1]]
    line1.set_data(x1, y1)
    line2.set_data(x2, y2)
    figure.canvas.draw_idle()

line1 = plt.plot(x1, y1, color="black", linewidth=3)[0]
line2 = plt.plot(x2, y2, color="black", linewidth=3)[0]
figure = plt.gcf()

root = tk.Tk()
root.geometry("600x200")
root.title("Forward Kinematics")

#--------Slider 1--------
h1 = tk.Label(root, text = "q1 angle (degrees)")
slider1 = tk.Scale(root, from_=0, to_=360, orient="horizontal", length=600, command=moveline1)
slider1.set(to_degrees(q1))
slider1.pack()
h1.pack()

#--------Slider 2--------
h2 = tk.Label(root, text = "q2 angle (degrees)")
slider2 = tk.Scale(root, from_=0, to_=360, orient="horizontal", length=600)
slider2.pack()
h2.pack()


plt.ylim(0, 12)
plt.xlim(0, 12)
plt.show()
tk.mainloop()
