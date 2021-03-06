#!/usr/bin/python3
###############################################################################
#Description: [WARNING]This stops and removes ALL docker images and containers.
#  Make sure you want to do this before you mess with it, because it is armed.
#  It is good for dropping and clearing my development machine. 
###############################################################################
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
        print('FileNotFoundError: Is docker installed?')
    else:
        print('An Error Occurred Stop All Containers')
         

def selRemoveAllContainers():
    aLabel.configure(text="Removing All Containers")
    p.run(['echo',\
            'Removing All Containers'])    
    c2 = 'docker ps -a | awk \'{ print $1 }\' | grep -v CONTAINER | xargs -I{} docker rm {}'
    l2 = c2.split(' ')
    try:
        p.run(l2)
    except FileNotFoundError:
        print('FileNotFoundError: Is docker installed?')
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
        print('FileNotFoundError: Is docker installed?')
    else:
        print('An Error Occurred Images All Containers')
  

def radCall():
    radSel=radVar.get()
    if   radSel == 1: selStopAllContainers
    elif radSel == 2: selRemoveAllContainers 
    elif radSel == 3: selRemoveAlContainers
    
var = tk.IntVar()
R1 = ttk.Radiobutton(win, text="Stop All Containers",\
        variable=var, value=1, command=radCall)
R1.grid(column=1, row=1, sticky=tk.W)
R2 = ttk.Radiobutton(win, text="Remove All Containers",\
        variable=var, value=2, command=radCall)
R2.grid(column=1, row=2, sticky=tk.W)
R3 = ttk.Radiobutton(win, text="Remove All Images",\
        variable=var, value=3, command=radCall)
R3.grid(column=1, row=3, sticky=tk.W)

win.mainloop()

