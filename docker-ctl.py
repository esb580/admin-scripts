#!/usr/bin/python3
import subprocess as p
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Docker Control GUI")

aLabel = ttk.Label(win, text="Docker Command: ")
aLabel.grid(column=0, row=0)

def selStopAllContainers():
    aLabel.configure(text="Stopping All Containers")
    p.run(['echo',\
            'Stopping All Containers'])    
    c1 = 'docker ps -a | awk \'{ print $1 }\' | grep -v CONTAINER | xargs -I{} docker stop {}'
    l1 = c1.split(' ')
    try:
        p.run(l1)
    except FileNotFoundError:
        print('FileNotFoundError')
    else:
        print('An Error Occurred Removing All Containers')
         

def selRemoveAllContainers():
    aLabel.configure(text="Removing All Containers")
    p.run(['echo',\
            'Removing All Containers'])    
    c2 = 'docker ps -a | awk \'{ print $1 }\' | grep -v CONTAINER | xargs -I{} docker rm {}'
    l2 = c2.split(' ')
    try:
        p.run(l2)
    except FileNotFoundError:
        print('FileNotFoundError')
    else:
        print('An Error Occurred Removing All Containers')
 
def selRemoveAllImages():
    aLabel.configure(text="Removing All Images")
    p.run(['echo',\
            'Removing All Images'])    
    c3 = 'docker images | awk \'{ print $3 }\' | grep -v IMAGE* | xargs -I{} docker rmi {}'
    l3 = c3.split(' ')
    try:
        p.run(l3)
    except FileNotFoundError:
        print('FileNotFoundError')
    else:
        print('An Error Occurred Removing All Containers')
  
var = tk.IntVar()
R1 = ttk.Radiobutton(win, text="Stop All Containers",\
        variable=var, value=1, command=selStopAllContainers)
R1.grid(column=1, row=1)
R2 = ttk.Radiobutton(win, text="Remove All Containers",\
        variable=var, value=2, command=selRemoveAllContainers)
R2.grid(column=1, row=2)
R3 = ttk.Radiobutton(win, text="Remove All Images",\
        variable=var, value=3, command=selRemoveAllImages)
R3.grid(column=1, row=3)

win.mainloop()

