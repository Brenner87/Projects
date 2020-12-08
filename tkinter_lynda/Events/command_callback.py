from tkinter import *
from tkinter import ttk

def main():
    root=Tk()
    button1 = ttk.Button(root, text='Click Me 1!', command= lambda: callback(1))
    button2 = ttk.Button(root, text='Click Me 2!', command= lambda: callback(2))
    button3 = ttk.Button(root, text='Click Me 3!', command= lambda: callback(3))
    button1.pack()
    button2.pack()
    button3.pack()



    root.mainloop()



def callback(number):
    print(number)


if __name__ == '__main__':
    main()