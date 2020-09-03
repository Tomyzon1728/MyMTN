
from tkinter import *
from PIL import Image,ImageTk
#Creating the foundational framework for the platform
plan =Tk()
plan.title("MyMTN")
#loading all images as PNG
load = Image.open('pull_down.png')
render = ImageTk.PhotoImage(load, master = plan)
load_1 = Image.open('envelope.png')
render_1 = ImageTk.PhotoImage(load_1, master = plan) 
load_2= Image.open('play.png')
render_2= ImageTk.PhotoImage(load_2, master = plan)
load_3 = Image.open('bundle.png')
render_3 = ImageTk.PhotoImage(load_3, master = plan)
load_4 = Image.open('More.png')
render_4 = ImageTk.PhotoImage(load_4, master = plan)  
load_5 = Image.open('Home.png')
render_5 = ImageTk.PhotoImage(load_5, master = plan) 
load_6 = Image.open('recharge.png')
render_6 = ImageTk.PhotoImage(load_6, master = plan)             
#Setting up Buttons on the Tool bar 
tool_bar=Label(plan,bg="#FFD700",borderwidth=2,relief = "flat")              
btn_a = Button(tool_bar,image= render,relief= 'flat')
btn_a.pack(side= 'left',anchor= 'w')
#----------------------------------------------
btn_b = Button(tool_bar,image= render_1,relief= 'flat')
btn_b.pack(side= 'right',anchor= 'w')
#----------------------------------------------

#closing toolbar               
tool_bar.pack(side=TOP,fill=X)
#Setting up Bottom toolbar

tool_bar2=Label(plan,bg="white",borderwidth=5,relief = "flat") 
#-----------------------------------------------
btn_d = Button(tool_bar2,image= render_4,relief= 'flat')
btn_d.pack(side= 'right',anchor= 'w')
btn_1 = Button(tool_bar2,bg="white",relief= 'flat')
btn_1.pack(side= 'right',anchor= 'w')
#----------------------------------------------
btn_c = Button(tool_bar2,image= render_2,relief= 'flat')
btn_c.pack(side= 'right',anchor= 'w')
btn_2 = Button(tool_bar2,bg="white",relief= 'flat')
btn_2.pack(side= 'right',anchor= 'w')
#----------------------------------------------
btn_e = Button(tool_bar2,image= render_3,relief= 'flat')
btn_e.pack(side= 'right',anchor= 'w')
btn_3 = Button(tool_bar2,bg="white",relief= 'flat')
btn_3.pack(side= 'right',anchor= 'w')
#---------------------------------------------------
btn_f = Button(tool_bar2,image= render_6,relief= 'flat')
btn_f.pack(side= 'right',anchor= 'w')
btn_4 = Button(tool_bar2,bg="white",relief= 'flat')
btn_4.pack(side= 'right',anchor= 'w')
#--------------------------------------------------------
btn_g = Button(tool_bar2,image= render_5,relief= 'flat')
btn_g.pack(side= 'left',anchor= 'w')
#closing toolbar               
tool_bar2.pack(side=BOTTOM,fill=X)

foundation = Frame(plan)
foundation.pack(side = 'top')
#----------------------------------------------------------
#Setting up a Canvas and ScrollBar
scroll_bar = Scrollbar(foundation)
scroll_bar.grid(row =1, column = 1,sticky = 'ns' )
#----------------------------------------
canvas= Canvas(foundation)
canvas.grid(row = 1, column  =0)
#Configuring both Canvas and Scrollbar
canvas.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=canvas.yview)

plan.mainloop()