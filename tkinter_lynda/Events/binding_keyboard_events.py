from tkinter import *
from tkinter import ttk

def main():
    root=Tk()

    #root.bind('<KeyPress>', key_press)
    root.bind('<Control-c>', lambda e: shortcut('Copy'))
    root.bind('<Control-v>', lambda e: shortcut('Paste'))



    root.mainloop()

def shortcut(action):
    print(action)

def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))



if __name__ == '__main__':
    main()