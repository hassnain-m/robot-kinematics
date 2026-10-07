import tkinter as tk
from tkdial import Dial

def on_change(name, dial):
    print(name, dial.get())

def make_dial(master, name):
    dial = Dial(
        master=master,
        color_gradient=("yellow", "red"),
        start=0, end=360,
        text=f"{name}: ",
        unit_length=10,
        scroll_steps=10,
        integer=True,
        command=lambda: on_change(name, dial),  # `dial` here is this call's own variable
    )
    return dial

app = tk.Tk()

dials = {}
for i in range(1, 7):
    name = f"Joint {i}"
    dials[name] = make_dial(app, name)
    dials[name].grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=10, pady=10)

app.mainloop()