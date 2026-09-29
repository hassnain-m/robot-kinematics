"""
Experiment with Forward Kinematics Here
"""

import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Forward Kinematics")

h1 = tk.Label(root, text = "q1 angle (degrees)")
slider1 = tk.Scale(root, from_=-360, to_=360, orient="horizontal", length=400)
slider1.pack()
h1.pack()


h2 = tk.Label(root, text = "q2 angle (degrees)")
slider2 = tk.Scale(root, from_=-360, to_=360, orient="horizontal", length=400)
slider2.pack()
h2.pack()


tk.mainloop()