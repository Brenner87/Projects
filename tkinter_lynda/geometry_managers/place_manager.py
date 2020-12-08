from tkinter import *
from tkinter import ttk


def main():
    root=Tk()
    root.geometry('640x480+200+200')
    yellow=ttk.Label(root, text='Yellow', background='yellow')
    blue = ttk.Label(root, text='Blue', background='blue')
    green = ttk.Label(root, text='Green', background='green')
    orange = ttk.Label(root, text='Orange', background='orange')
    yellow.place(x=100, y=50, width=100, height=50)
    blue.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5, relheight=0.5)
    green.place(relx=0.5, x=100, rely=0.5, y=50)
    orange.place(relx=1.0, x=-5, y=5, anchor='ne')


    #place_slaves()
    #place.configure()
    #place.info()
    #place.forget()
    root.mainloop()


if __name__ == '__main__':
    main()