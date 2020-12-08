#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re



def main():
    root = Tk()
    root.title('Knitting')
    root.resizable(False, False)
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    main = App(root)
    main.grid()
    root.mainloop()

class App(Frame):
    def __init__(self, parent):
        super(App, self).__init__(parent)
        self.createInterface()
        self.draw()
        self.params={}

    def createInterface(self):
        self.row_num = StringVar()
        self.starting_from = StringVar()
        self.rows_in_block = StringVar()
        self.adding_each = StringVar()
        self.results_num = StringVar()

        #==LABELS===============
        self.row_num_label = Label(text='Введите количество рядов(*):')
        self.rows_in_block_label = Label(text='Введите колличество рядов в 1 блоке(*):')
        self.adding_each_label = Label(text='Введите ряды, в которых планируется расширение(через запятую)(*):')
        self.starting_from_label = Label(text='Введите номер ряда, с которого начинать отсчет:')
        self.results_num_label = Label(text='Введите колличество расширений:')
        self.answer_label = Label()

        #==ENTRIES==============
        self.row_num_entry = Entry(width=10, textvariable=self.row_num)
        self.rows_in_block_entry = Entry(width=10, textvariable=self.rows_in_block)
        self.adding_each_entry = Entry(width=10, textvariable=self.adding_each)
        self.starting_from_entry = Entry(width=10, textvariable=self.starting_from)
        self.results_num_entry = Entry(width=10, textvariable=self.results_num)

        #==BUTTONS==============
        self.calculate_button = Button(text='Посчитать', command=self.actionOnClick)

    def draw(self):
        #==LABELS===============
        self.row_num_label.grid(row=1, column=0, sticky=E)
        self.rows_in_block_label.grid(row=2, column=0, sticky=E)
        self.adding_each_label.grid(row=3, column=0, sticky=E)
        self.starting_from_label.grid(row=4, column=0, sticky=E)
        self.results_num_label.grid(row=5, column=0, sticky=E)

        self.answer_label.grid(row=6, column=0, columnspan=2)

        #==Entries=============
        self.row_num_entry.grid(row=1, column=1, sticky=E)
        self.rows_in_block_entry.grid(row=2, column=1, sticky=E)
        self.adding_each_entry.grid(row=3, column=1, sticky=E)
        self.starting_from_entry.grid(row=4, column=1, sticky=E)
        self.results_num_entry.grid(row=5, column=1, sticky=E)

        #==Buttons=============
        self.calculate_button.grid(row=7, column=0, columnspan=2, sticky='ew')

    def validateInput(self):
        self.params = {}

        row_num = self.row_num.get()
        try:
            row_num = int(row_num)
        except ValueError:
            self.answer_label['text'] = 'Можно вводить только цифровые значение. {} не подходит'.format(row_num)
            self.answer_label['fg'] = 'red'
            return
        self.params['row_num'] = row_num

        rows_in_block = self.rows_in_block.get()
        try:
            rows_in_block = int(rows_in_block)
        except ValueError:
            self.answer_label['text'] = 'Можно вводить только цифровые значение. {} не подходит'.format(rows_in_block)
            self.answer_label['fg'] = 'red'
            return
        self.params['rows_in_block'] = rows_in_block

        adding_each = self.adding_each.get()
        if re.match(r'^[\d,]*$', adding_each):
            self.params['adding_each'] = list(map(int, adding_each.split(',')))
        else:
            self.answer_label['text'] = 'Ряды в которых планируетя расширение должны выглядеть как список целых чисел черз запятую (без пробелов)'
            return

        starting_from = self.starting_from.get()
        if starting_from:
            try:
                starting_from = int(starting_from)
            except ValueError:
                self.answer_label['text'] = 'Можно вводить только цифровые значение. {} не подходит'.format(starting_from)
                self.answer_label['fg'] = 'red'
                return
            if self.params.get('row_num') and starting_from >= self.params.get('row_num'):
                self.answer_label['text'] = 'Начальный ряд не может быть больше количества рядов.'
                self.answer_label['fg'] = 'red'
                return
            self.params['starting_from'] = starting_from

        results_num = self.results_num.get()
        if results_num:
            try:
                results_num = int(results_num)
            except ValueError:
                self.answer_label['text'] = 'Можно вводить только цифровые значение. {} не подходит'.format(results_num)
                self.answer_label['fg'] = 'red'
                return
        self.answer_label['text'] =''
        self.answer_label['fg'] = 'black'
        self.params['results_num'] = results_num
        return True

    def actionOnClick(self):
        if self.validateInput():
            results = self.calculate_nums_in_block(**self.params)
            print(self.params)
            self.answer_label['text'] = ' '.join(map(str, results))

    def calculate_nums_in_block(self, row_num, rows_in_block, adding_each, results_num=None, starting_from=None):
        count = 0
        results = []
        start_pos = starting_from or 1
        for i in range(start_pos, row_num + 1):
            count += 1
            if adding_each[0] == count:
                adding_each.append(adding_each.pop(0))
                count = 0
                num_in_block = i % rows_in_block or rows_in_block
                results.append(num_in_block)
        if results_num and len(results) > results_num:
            return results[:results_num]
        return results



if __name__ == '__main__':
    main()