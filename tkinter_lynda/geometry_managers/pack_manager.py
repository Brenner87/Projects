from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    #ttk.Label(root, text='Hello, Tkinter!', background='yellow').pack(fill=X)
    #ttk.Label(root, text='Hello, Tkinter!', background='yellow').pack(fill=Y)
    #ttk.Label(root, text='Hello, Tkinter!', background='yellow').pack(fill=BOTH, expand=True)
    label=ttk.Label(root, text='Hello, Tkinter!', background='yellow')
    label.pack(side=LEFT, anchor='nw')
    ttk.Label(root, text='Hello, Tkinter!', background='blue').pack(side=LEFT, padx=10, pady=10)
    ttk.Label(root, text='Hello, Tkinter!', background='green').pack(side=LEFT, ipadx=10, ipady=10)
    for widget in root.pack_slaves():
        widget.pack_configure(fill=BOTH, expand=True)
        print(widget.pack_info())
    label.pack_forget()


    root.mainloop()






if __name__ == '__main__':
    main()