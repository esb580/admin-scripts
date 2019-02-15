#!/usr/bin/python3
import subprocess
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Docker Control GUI")

aLabel = ttk.Label(win, text="Docker Command: ")
aLabel.grid(column=0, row=0)

def executeCommand():
    action.configure(text="Run Command")
    aLabel.configure(text="A Red Label")

def selStopAllContainers():
    aLabel.configure(text="Stopping All Containers")

def selRemoveAllContainers():
    aLabel.configure(text="Removing All Containers")

def selRemoveAllImages():
    aLabel.configure(text="Removing All Images")


#action = ttk.Button(win, text="Execute", command=executeCommand)
#action.grid(column=1, row=0)

var = tk.IntVar()
R1 = ttk.Radiobutton(win, text="Stop All Containers", variable=var, value=1, command=selStopAllContainers)
R1.grid(column=1, row=1)
R2 = ttk.Radiobutton(win, text="Remove All Containers", variable=var, value=2, command=selRemoveAllContainers)
R2.grid(column=1, row=2)
R3 = ttk.Radiobutton(win, text="Remove All Images", variable=var, value=3, command=selRemoveAllImages)
R3.grid(column=1, row=3)

win.mainloop()

