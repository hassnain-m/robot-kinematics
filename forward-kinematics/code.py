import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, q1, q2, l1, l2):
        self.q1 = q1
        self.q2 = q2
        self.l1 = l1
        self.l2 = l2

    def get_joints(self): #return the coordinates of joints a and b
        a = [np.cos(self.q1)*self.l1, np.sin(self.q1)*self.l1]
        b = [a[0]+np.cos(self.q1 + self.q2) * self.l2, a[1]+np.sin(self.q1 + self.q2) * self.l2]
        return a,b

    def change_q1(self, new_q1):
        self.q1 = new_q1

    def change_q2(self, new_q2):
        self.q2 = new_q2

class RobotPlotter:
    def __init__(self, robot, figure):
        self.robot = robot
        self.figure = figure

        a, b = self.robot.get_joints()
        self.base_joint = plt.plot(0, 0, "ro")[0]

        line1x = [0, a[0]]
        line1y = [0, a[1]]

        line2x = [a[0], b[0]]
        line2y = [a[1], b[1]]

        self.joint_a = plt.plot(a[0], a[1], "ro")[0]
        self.joint_b = plt.plot(b[0], b[1], "ro")[0]

        self.line1 = plt.plot(line1x, line1y, color="black", linewidth=3)[0]
        self.line2 = plt.plot(line2x, line2y, color="black", linewidth=3)[0]

    def draw(self):
        a, b = self.robot.get_joints()

        line1x = [0, a[0]]
        line1y = [0, a[1]]

        line2x = [a[0], b[0]]
        line2y = [a[1], b[1]]


        self.line1.set_data(line1x, line1y)
        self.line2.set_data(line2x, line2y)

        self.joint_a.set_data([a[0]], [a[1]])
        self.joint_b.set_data([b[0]], [b[1]])

        self.figure.canvas.draw_idle()


#--------Initial Values and Setup--------
l1 = 5  #length of first link
l2 = 5 #length of second link
q1 = np.pi/4 #q1 starting angle in radians
q2 = np.pi/4 #q2 starting angle in radians

figure = plt.gcf()
robot = Robot(q1, q2, l1, l2)
plotter = RobotPlotter(robot, figure)

root = tk.Tk()
root.geometry("600x200")
root.title("Forward Kinematics")


#--------methods--------
def to_degrees(value):
    return float(value) * 180 / np.pi

def to_radians(value):
    return float(value) * np.pi / 180


def on_q1_changed(q1):
    q1_radians = to_radians(q1)
    robot.change_q1(q1_radians)
    plotter.draw()

def on_q2_changed(q2):
    q2_radians = to_radians(q2)
    robot.change_q2(q2_radians)
    plotter.draw()

#--------Slider 1--------
h1 = tk.Label(root, text = "q1 angle (degrees)")
slider1 = tk.Scale(root, from_=-180, to_=180, orient="horizontal", length=600, command=on_q1_changed)
slider1.set(to_degrees(q1))
slider1.pack()
h1.pack()

#--------Slider 2--------
h2 = tk.Label(root, text = "q2 angle (degrees)")
slider2 = tk.Scale(root, from_=-180, to_=180, orient="horizontal", length=600, command=on_q2_changed)
slider2.set(to_degrees(q2))
slider2.pack()
h2.pack()

plt.ylim(0, 12)
plt.xlim(0, 12)
plt.show()
tk.mainloop()