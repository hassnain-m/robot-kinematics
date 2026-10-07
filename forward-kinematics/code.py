import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, q1, q2, l1, l2): #initialise the link lengths and joint angles as instance variables
        self.q1 = q1
        self.q2 = q2
        self.l1 = l1
        self.l2 = l2

    def get_joints(self): #return the coordinates of joints a and b
        a = [np.cos(self.q1)*self.l1, np.sin(self.q1)*self.l1]
        b = [a[0]+np.cos(self.q1 + self.q2) * self.l2, a[1]+np.sin(self.q1 + self.q2) * self.l2]
        return a,b

    def set_q1(self, new_q1): #update the value of q1
        self.q1 = new_q1

    def set_q2(self, new_q2): #update the value of q2
        self.q2 = new_q2

class RobotPlotter:
    def __init__(self, robot, figure): #initialise the RobotPlotter. robot is a Robot object and figure is a matplotlib figure
        self.robot = robot
        self.figure = figure

        a, b = self.robot.get_joints() #obtain the joint coordinates of a and b, and set them as local variables
        self.base_joint = plt.plot(0, 0, "ro")[0] #draw a marker at the base joint

        line1x = [0, a[0]] #x values of origin and a
        line1y = [0, a[1]] #y values of origin and a

        line2x = [a[0], b[0]] #x values of a and b
        line2y = [a[1], b[1]] #y values of a and b


        self.line1 = plt.plot(line1x, line1y, color="black", linewidth=3)[0] #draw the initial line between the origin and a, and store in the instance variable line1
        self.line2 = plt.plot(line2x, line2y, color="black", linewidth=3)[0] #draw the second line between a and b, and store in the instance variable line2

        self.joint_a = plt.plot(a[0], a[1], "ro")[0] #draw the initial marker at joint a
        self.joint_b = plt.plot(b[0], b[1], "ro")[0] #draw the initial marker at joint b

    def draw(self):
        a, b = self.robot.get_joints() #obtain the joint coordinates of the robot from the robot class and keep them stored as joints a and b

        line1x = [0, a[0]] #store the x coordinates of 2 points that lie on line 1; origin and a
        line1y = [0, a[1]] #store the y coordinates of 2 points that lie on line 1; origin and a

        line2x = [a[0], b[0]] #store the x coordinates of 2 points that lie on line 2; a and b
        line2y = [a[1], b[1]] #store the y coordinates of 2 points that lie on line 2; a and b


        self.line1.set_data(line1x, line1y) #update the line1 plot to the new line1x and line1y coordinates
        self.line2.set_data(line2x, line2y) #update the line2 plot to the new line2x and line2y coordinates

        self.joint_a.set_data([a[0]], [a[1]]) #update the red marker indicating where the joint at a is
        self.joint_b.set_data([b[0]], [b[1]]) #update the red marker indicating where the joint at b is

        self.figure.canvas.draw_idle() #tell Matplotlib to redraw the figure when it gets a chance, rather than forcing an immediate redraw. Useful when the plot is being updated repeatedly, such as when moving a slider


#--------Initial Values and Setup--------
l1 = 5  #length of first link
l2 = 5 #length of second link
q1 = np.pi/4 #q1 starting angle in radians
q2 = -np.pi/4 #q2 starting angle in radians

figure = plt.gcf() #get the current plot figure
robot = Robot(q1, q2, l1, l2) #instantiate a Robot object
plotter = RobotPlotter(robot, figure) #instantiate a RobotPlotter object

root = tk.Tk() # create the main Tkinter window
root.geometry("600x200")
root.title("Forward Kinematics")


#--------methods--------
def to_degrees(value): #convert radians to degrees
    return float(value) * 180 / np.pi

def to_radians(value): #convert degrees to radians
    return float(value) * np.pi / 180


def on_q1_changed(q1): #this function is called when the q1 slider is changed; what to do when q1 changes
    q1_radians = to_radians(q1)
    robot.set_q1(q1_radians)
    plotter.draw() #update the plot

def on_q2_changed(q2): #this function is called when the q2 slider is changed; what to do when q2 changes
    q2_radians = to_radians(q2)
    robot.set_q2(q2_radians)
    plotter.draw() #update the plot

#--------Slider 1--------
h1 = tk.Label(root, text = "q1 angle (degrees)")
slider1 = tk.Scale(root, from_=-180, to_=180, orient="horizontal", length=600, command=on_q1_changed)
slider1.set(to_degrees(q1))
slider1.pack() #add slider1 to the gui
h1.pack() #add h1 to the gui

#--------Slider 2--------
h2 = tk.Label(root, text = "q2 angle (degrees)")
slider2 = tk.Scale(root, from_=-180, to_=180, orient="horizontal", length=600, command=on_q2_changed)
slider2.set(to_degrees(q2))
slider2.pack() #add slider2 to the gui
h2.pack() #add h2 to the gui

plt.xlim(0, 12) #set x axis limit
plt.ylim(0, 12) #set y axis limit
plt.show()
tk.mainloop()