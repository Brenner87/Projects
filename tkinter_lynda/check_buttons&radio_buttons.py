from tkinter import *
from tkinter import ttk
root=Tk()
checkbutton=ttk.Checkbutton(root, text='SPAM?')
checkbutton.pack()

spam=StringVar()
spam.set('SPAM!')
print(spam.get())
checkbutton.config(variable=spam, onvalue='SPAM Please!', offvalue='Boo SPAM')
breakfast=StringVar()
radiobutton1=ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
radiobutton2=ttk.Radiobutton(root, text='Aggs', variable=breakfast, value='Aggs').pack()
radiobutton3=ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sauages').pack()
radiobutton4=ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
checkbutton.config(textvariable=breakfast)

root.mainloop()
