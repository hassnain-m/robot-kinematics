"""
Experiment with Forward Kinematics Here
"""

import tkinter as tk

def value_changed(value):
    print(int(float(value)))

root = tk.Tk()
root.geometry("400x200")
root.title("Forward Kinematics")

h1 = tk.Label(root, text = "q1 angle (degrees)")
slider1 = tk.Scale(root,
                   from_=-360,
                   to_=360,
                   orient="horizontal",
                   length=400)

h2 = tk.Label(root, text = "q2 angle (degrees)")
slider2 = tk.Scale(root,
                   from_=-360,
                   to_=360,
                   orient="horizontal",
                   length=400,
                   command=value_changed
)

slider1.pack()
h1.pack()
slider2.pack()
h2.pack()

s1_val = slider1.get()
s2_val = slider2.get()


root.mainloop()