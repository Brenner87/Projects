from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

def main():
    messagebox.showinfo(title='A Friendly Message', message='Hello Tkinter')
    filename=filedialog.askopenfile()
    print(filename)
    print(filename.name)
    color=colorchooser.askcolor(initialcolor='#FFFFFF')
    print(color)





if __name__ == '__main__':
    main()