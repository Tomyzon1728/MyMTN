# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 04:31:21 2020

@author: Ajayi Raymond T
"""

from tkinter import *
from PIL import Image,ImageTk

foundation =Tk()
foundation.title("MyMTN")
top_label=Label(foundation,bg="#FFD700")
top_label.pack(fill=X)

load = Image.open('pull_down.png')
render = ImageTk.PhotoImage(load, master = foundation)
btn_a = Button(top_label,image= render,relief= 'flat')
btn_a.pack(side= 'left',anchor= 'w')

load_1 = Image.open('envelope.png')
render_1 = ImageTk.PhotoImage(load_1, master = foundation)
btn_b = Button(top_label,image= render_1,relief= 'flat')
btn_b.pack(side= 'right',anchor= 'w')
#btnn = Button(top_label,image= rendern,relief= 'flat')
#btnn.pack(side= 'left',anchor= 'w')


foundation.mainloop()