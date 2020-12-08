from tkinter import *
from tkinter import ttk

def main():
    root=Tk()
    button=ttk.Button(root, text="Click Me")
    button.pack()
    button.config(command=callback)
    button.invoke()
    button.state(['disabled'])
    print(button.instate(['disabled']))
    button.state(['!disabled'])
    print(button.instate(['!disabled']))
    logo=PhotoImage(file='python_logo.gif')
    button.config(image=logo, compound=LEFT)
    small_logo=logo.subsample(5,5)
    button.config(image=small_logo)

    root.mainloop()



def callback():
    print ('Clicked')



if __name__=='__main__':
    main()
