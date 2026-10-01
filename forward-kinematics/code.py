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
l1 = 5  #length of first link
l2 = 5 #length of second link
q1 = np.pi/4 #q1 starting angle in radians
q2 = np.pi #q2 starting angle in radians

x0, y0 = [0, 0] #origin's x and y
o = [x0, y0] #orgin

x1, y1 = [o[0] + np.cos(q1) * l1, o[1] + np.sin(q1) * l1]
a = [x1, y1] #coordinates of first joint

x2, y2 = [a[0] + np.cos(q2) * l1, a[1] + np.sin(q2) * l1]
b = [x2, y2] #coordinates of second joint

line1x = [x0, x1] #line 1's x coordinates; the x values of 2 coordinates that lie on line 1
line1y = [y0, y1] #line 1's y coordintes; the y values of 2 coordinates that lie on line 1
line2x = [x1, x2] #line 2's x coordinates; the x values of 2 coordinates that lie on line 2
line2y = [y1, y2] #line 2's y coordintes; the y values of 2 coordinates that lie on line 2

def moveline1(q1_in_degrees):
    q1 = to_radians(q1_in_degrees)
    a = [np.cos(q1) * l1, np.sin(q1) * l1]
    line1x, line1y = [o[0], a[0]], [o[1], a[1]]
    b = [a[0] + (np.cos(q2) * l1), a[1] + (np.sin(q2) * l1)]
    line2x, line2y = [a[0], b[0]], [a[1], b[1]]
    line1.set_data(line1x, line1y)
    line2.set_data(line2x, line2y)
    figure.canvas.draw_idle()

def moveline2(q2_in_degrees):
    q2 = to_radians(q2_in_degrees)



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
