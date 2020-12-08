from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def main():
    root=Tk()
    feedback=Feedback(root)
    feedback.name.insert(0,'hi there')
    root.mainloop()






class Feedback:
    def __init__(self, master):
        #master.geometry('400x300')
        #master.columnconfigure(0, weight=2)
        #master.columnconfigure(1,weight=3)
        #master.config(background="#fff")
        master.title('Explore California Feedback')
        master.resizable(False, False)
        master.configure(background='#e1d8b9')
        self.style=ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 11))
        self.style.configure('Header.TLabel', background='#e1d8b9', font=('Arial', 18, 'bold'))
        self.leftPad=5

        self.frameHeader=ttk.Frame(master)

        self.logo = PhotoImage(file='tour_logo.gif')
        self.logoframe = ttk.Label(self.frameHeader, image=self.logo)
        self.header = ttk.Label(self.frameHeader, text='Feedback form', style='Header.TLabel')
        self.headerSurvMess = ttk.Label(self.frameHeader, wraplength=300, text='What do you think about our tour?')


        self.frameContent=ttk.Frame(master)
        self.name = ttk.Entry(self.frameContent, width=24)
        self.nameLabel=ttk.Label(self.frameContent, text='Name:')
        self.email=ttk.Entry(self.frameContent, width=24)
        self.emailLabel = ttk.Label(self.frameContent, text='Email:')

        self.feedbackLabel=ttk.Label(self.frameContent, text='Comment:')
        self.feedbackBody=Text(self.frameContent, cursor='man', wrap='word', width=66, height=10, font=('Arial', 10))

        self.clearButton=ttk.Button(self.frameContent, text='Clear', command=self.actionOnClear)


        self.submitButton = ttk.Button(self.frameContent, text='Submit', command=self.actionOnSubmit)



        self.frameHeader.grid(row=0, column=0, stick='nswe')

        self.logoframe.grid(row=0, column=0, rowspan=2)
        self.header.grid(row=0, column=1)
        self.headerSurvMess.grid(row=1, column=1)



        self.frameContent.grid(row=1, column=0, stick='nswe')

        self.nameLabel.grid(row=0, column=0, stick='sw', padx=5)
        self.name.grid(row=1, column=0, stick='sw', padx=5)
        self.emailLabel.grid(row=0, column=1, stick='sw', padx=5)
        self.email.grid(row=1, column=1, stick='sw', padx=5)
        self.feedbackLabel.grid(row=2, column=0, stick='sw', padx=5)
        self.feedbackBody.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        self.clearButton.grid(row=4, column=0, padx=5, stick='e')
        self.submitButton.grid(row=4, column=1, padx=5, stick='w')


    def actionOnClear(self):
        self.name.delete('0','end')
        self.email.delete(0, 'end')
        self.feedbackBody.delete('1.0','end')



    def actionOnSubmit(self):
        self.nameVar=self.name.get()
        self.emailVar=self.email.get()
        self.feedbackVar=self.feedbackBody.get('1.0', 'end')
        self.actionOnClear()
        print('Name: {}\nEmail: {}\nFeedback:\n{}'.format(self.nameVar, self.emailVar, self.feedbackVar))
        messagebox.showinfo(title='Explore California Feedback', message='Comments Submitted!')




if __name__ == '__main__':
    main()