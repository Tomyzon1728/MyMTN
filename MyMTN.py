# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 04:31:21 2020

@author: Ajayi Raymond T
"""

from tkinter import *
from PIL import Image,ImageTk
#Creating the foundational framework for the platform
foundation =Tk()
foundation.title("MyMTN")
tool_bar=Frame(foundation,bg="#FFD700",borderwidth=2,relief = "flat")
#Setting up the Tool bar               
load = Image.open('pull_down.png')
render = ImageTk.PhotoImage(load, master = foundation)
btn_a = Button(tool_bar,image= render,relief= 'flat')
btn_a.pack(side= 'left',anchor= 'w')
#----------------------------------------------
load_1 = Image.open('envelope.png')
render_1 = ImageTk.PhotoImage(load_1, master = foundation)
btn_b = Button(tool_bar,image= render_1,relief= 'flat')
btn_b.pack(side= 'right',anchor= 'w')
#closing toolbar               
tool_bar.pack(side=TOP,fill=X)
#----------------------------------------------------------
#Setting up a Canvas and ScrollBar
scroll_bar = Scrollbar(foundation)
scroll_bar.pack(side=RIGHT, fill=Y)
#----------------------------------------
canvas= Canvas(foundation)
canvas.pack()
#Configuring both Canvas and Scrollbar
canvas.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=canvas.yview)

foundation.mainloop()