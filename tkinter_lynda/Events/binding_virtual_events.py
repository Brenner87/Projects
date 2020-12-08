from tkinter import *
from tkinter import ttk



def main():
    root=Tk()
    entry=ttk.Entry(root)
    entry.pack()

    entry.bind('<<Copy>>', lambda e: print('Copy'))
    entry.bind('<<Paste>>', lambda e: print('Paste'))
    entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
    entry.bind('<<OddNumber>>', lambda e: print('Odd Number'))

    print(entry.event_info('<<OddNumber>>'))
    print(entry.event_info('<<Paste>>'))
    entry.event_generate('<<OddNumber>>')
    entry.event_generate('<<Paste>>')
    #entry.event_delete('<<OddNumber>>')



    root.mainloop()




if __name__ == '__main__':
    main()