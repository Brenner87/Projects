from tkinter import *
from tkinter import ttk
def main():
    root=Tk()
    entry=ttk.Entry(root, width=30)
    entry.pack()
    content = entry.get()
    print(content)
    entry.delete(0,1)
    entry.delete(0, END)
    entry.insert(0,'Enter your password')
    entry.config(show='*')
    entry.state(['disabled'])
    entry.state(['!disabled'])
    entry.state(['readonly'])


    root.mainloop()





if __name__=='__main__':
    main()