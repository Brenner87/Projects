from tkinter import *
from tkinter import ttk



def main():
    root=Tk()

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=3)

    root.columnconfigure(2, weight=1)


    yellow=ttk.Label(root, text='Yellow', background='Yellow')
    blue = ttk.Label(root, text='Blue', background='Blue')
    green = ttk.Label(root, text='Green', background='Green')
    orange = ttk.Label(root, text='Orange', background='Orange')
    #yellow.grid(row=1, column=1)
    #blue.grid(row=1, column=0)
    #green.grid(row=0, column=0)
    #orange.grid(row=0, column=1)

    yellow.grid(row=0, column=2, rowspan=2, stick='nsew')
    blue.grid(row=1, column=0, columnspan=2, stick='nsew')
    green.grid(row=0, column=0, stick='nsew', padx=10, pady=10)
    orange.grid(row=0, column=1, stick='nsew', ipadx=25, ipady=25)

    root.mainloop()





if __name__ == '__main__':
    main()