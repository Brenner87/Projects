from tkinter import *
from tkinter import ttk
root=Tk()
frame=ttk.Frame(root)
frame.pack()
frame.config(height=100, width=200)
frame.config(relief=RIDGE)
ttk.Button(frame, text='Click Me').grid()
frame.config(padding=(30,15))
frame2=ttk.LabelFrame(root, height=100, width=200, text='My Frame').pack()



root.mainloop()

#Reliefs: FLAT RAISED SUNKEN SOLID RIDGE GROOVE

