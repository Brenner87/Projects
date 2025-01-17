from tkinter import *
from tkinter import ttk



def main():
    root=Tk()
    button1=ttk.Button(root, text='Button 1')
    button2=ttk.Button(root, text='Button 2')
    button1.pack()
    button2.pack()
    style = ttk.Style()
    print(style.theme_names())
    print (style.theme_use())
    style.theme_use('classic')
    style.theme_use('vista')
    print(button1.winfo_class())
    style.configure('TButton', foreground='blue')
    style.configure('Alarm.TButton', foreground='orange', font=('Arial', 24, 'bold'))
    button2.config(style='Alarm.TButton')
    style.map('Alarm.TButton', foreground=[('pressed', 'pink'), ('disabled', 'grey')])
    #button2.state(['disabled'])
    print(style.layout('TButton'))
    print(style.element_options('Button.label'))
    print(style.element_options('Button.padding'))
    print(style.element_options('Button.focus'))
    print(style.element_options('Button.button'))
    print(style.lookup('TButton', 'foreground'))





    root.mainloop()



if __name__ == '__main__':
    main()
