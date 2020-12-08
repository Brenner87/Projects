from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from file_handle import *
from datetime import *
from statistics import *

log=logging.getLogger(__name__)
log.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
#file_handler=logging.FileHandler('logging_test_2.log')
#file_handler.setFormatter(formatter)
#logger.addHandler(file_handler)
streamhandler=logging.StreamHandler()
streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)


def main():
    root=Tk()
    myApp=myInterface(root)
    root.mainloop()


class myInterface:
    def __init__(self, master):
        self.master=master
        self.createInterface()
        self.drowInterface()




    def createInterface(self):
        bgcolor='#CCCCFF'
        widgTitle='Lake Pend Oreille'
        widgImgText='Lake Pend Oreille\nWether Statistics'
        days = [i for i in range(1, 32)]
        self.months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
        self.master.title(widgTitle)
        self.master.resizable(False, False)
        self.master.configure(background=bgcolor)
        self.style=ttk.Style()
        self.style.configure('TFrame', background=bgcolor)
        self.style.configure('TButton', background=bgcolor)
        self.style.configure('TLabel', background=bgcolor)
        self.style.configure('TFrame', background=bgcolor)
        self.years=[i for i in range(2012,2016)]
        self.startDay=StringVar()
        self.startMonth=StringVar()
        self.startYear=StringVar()
        self.endDay=StringVar()
        self.endMonth=StringVar()
        self.endYear=StringVar()

    #stuff for frame1
        self.frame1 = ttk.Frame(self.master)

        #Logo and header
        self.logo=PhotoImage(file='transformers-logo.gif').subsample(2,2)
        self.logoLable=ttk.Label(self.frame1, text=widgImgText, image=self.logo, compound='center', font=('Courier', 15, 'bold'), foreground='white')

        #text labels
        self.labelStartDate=ttk.Label(self.frame1, text='Start Date:')
        self.labelEndDate=ttk.Label(self.frame1, text='End Date:')

        # combo boxes
        self.startDayBox = Spinbox(self.frame1, textvariable=self.startDay, values=days, width=2)
        self.startMonthBox = Spinbox(self.frame1, textvariable=self.startMonth, values=self.months, width=3, state='readonly')
        self.startYearBox = Spinbox(self.frame1, textvariable=self.startYear, values=self.years, width=4)
        self.endDayBox = Spinbox(self.frame1, textvariable=self.endDay, values=days, width=2)
        self.endMonthBox = Spinbox(self.frame1, textvariable=self.endMonth, values=self.months, width=3, state='readonly')
        self.endYearBox = Spinbox(self.frame1, textvariable=self.endYear, values=self.years, width=4)

        #buttons
        self.submitButton = ttk.Button(self.frame1, text='Submit', command=self.actionOnSubmit)


    #stuff for frame2
        self.frame2 = ttk.Frame(self.master)

        #text labels
        self.labelWindSpeed=ttk.Label(self.frame2, text='Wind\nSpeed:')
        self.labelAirTemp=ttk.Label(self.frame2, text='Air\nTemp:')
        self.labelPressure=ttk.Label(self.frame2, text='Barometric\nPressure:')
        self.labelMean=ttk.Label(self.frame2, text='Mean:')
        self.labelMedian=ttk.Label(self.frame2, text='Median:')

        #labels for result output
        self.labelWindMean=ttk.Label(self.frame2)
        self.labelWindMedian = ttk.Label(self.frame2)
        self.labelTempMean = ttk.Label(self.frame2)
        self.labelTempMedian = ttk.Label(self.frame2)
        self.labelPresMean = ttk.Label(self.frame2)
        self.labelPresMedian = ttk.Label(self.frame2)




    def drowInterface(self):
        self.frame1.grid()
        self.logoLable.grid(row=0, column=0, columnspan=6)
        self.labelStartDate.grid(row=1, column=0, columnspan=3, stick='nw')
        self.labelEndDate.grid(row=1, column=3, columnspan=3, stick='nw')

        self.startDayBox.grid(row=2, column=0)
        self.startMonthBox.grid(row=2, column=1)
        self.startYearBox.grid(row=2, column=2)
        self.endDayBox.grid(row=2, column=3)
        self.endMonthBox.grid(row=2, column=4)
        self.endYearBox.grid(row=2, column=5)
        self.submitButton.grid(row=3, column=2, columnspan=2)

        self.labelMean.grid(row=1, column=0, columnspan=2)
        self.labelMedian.grid(row=2, column=0, columnspan=2)
        self.labelWindSpeed.grid(row=0, column=3)
        self.labelAirTemp.grid(row=0, column=4)
        self.labelPressure.grid(row=0, column=5, columnspan=2)

        self.labelWindMean.grid(row=1,column=3)
        self.labelWindMedian.grid(row=2, column=3)
        self.labelTempMean.grid(row=1, column=4)
        self.labelTempMedian.grid(row=2, column=4)
        self.labelPresMean.grid(row=1, column=5)
        self.labelPresMedian.grid(row=2, column=5)


    def actionOnSubmit(self):
        if self.validateInput() is None:
            return
        startDate, endDate=self.validateInput()
        handler=dataHandler(startDate, endDate)
        results=self.calculateData(handler.fileContent)
        self.labelWindMean.configure(text=str(round(results[0], 2)))
        self.labelTempMean.configure(text=str(round(results[1], 2)))
        self.labelPresMean.configure(text=str(round(results[2], 2)))
        self.labelWindMedian.configure(text=str(round(results[3], 2)))
        self.labelTempMedian.configure(text=str(round(results[4], 2)))
        self.labelPresMedian.configure(text=str(round(results[5], 2)))
        self.frame2.grid()

    def validateInput(self):
        if int(self.startYear.get()) not in self.years or int(self.endYear.get()) not in self.years:
            output='year should be between {} and {}.\nPlease try again'\
                .format(str(self.years[0]), str(self.years[-1]))
            log.error(output)
            messagebox.showinfo(title='Invalid Input', message=output)
            return None
        try:
            startDate = date(int(self.startYear.get()),
                             self.months.index(self.startMonth.get()) + 1,
                             int(self.startDay.get()))

            endDate = date(int(self.endYear.get()),
                           self.months.index(self.endMonth.get()) + 1,
                           int(self.endDay.get()))
            return startDate, endDate
        except Exception as err:
            output='{}\nPlease try again'.format(err)
            log.error(output)
            messagebox.showinfo(title='Invalid Input', message=output)
            return None

    def calculateData(self, inputData):
        windSpeed=[]
        airTemp=[]
        pressure=[]
        for i in inputData:
            windSpeed.append(i[-1])
            airTemp.append(i[1])
            pressure.append(i[2])
        return [*map(mean, [windSpeed, airTemp, pressure]), *map(median, [windSpeed, airTemp, pressure])]





if __name__ == '__main__':
    main()