#!/usr/bin/python3
import sys
import re

def main():
    row_num = input('Введите количество рядов(*): ')
    try:
        row_num = int(row_num)
    except ValueError:
        print('Можно вводить только цифровые значение. {} не подходит'.format(row_num))
        sys.exit(1)

    rows_in_block = input('Введите колличество рядов в 1 блоке(*): ')
    try:
        rows_in_block = int(rows_in_block)
    except ValueError:
        print('Можно вводить только цифровые значение. {} не подходит'.format(rows_in_block))
        sys.exit(1)

    adding_each = input('Введите ряды, в которых планируется расширение(через запятую)(*): ')
    if re.match(r'^[\d,]*$', adding_each):
        adding_each = list(map(int, adding_each.split(',')))
    else:
        print('Ряды в которых планируетя расширение должны выглядеть как список целых чисел черз запятую (без пробелов)')
        sys.exit(1)

    starting_from = input('Введите номер ряда, с которого начинать отсчет: ')
    if starting_from:
        try:
            starting_from = int(starting_from)
        except ValueError:
            print('Можно вводить только цифровые значение. {} не подходит'.format(starting_from))
            sys.exit(1)
        if starting_from >= row_num:
            print('Начальный ряд не может быть больше количества рядов.')
            sys.exit(1)

    results_num = input('Введите колличество расширений: ')
    if results_num:
        try:
            results_num = int(results_num)
        except ValueError:
            print('Можно вводить только цифровые значение. {} не подходит'.format(results_num))
            sys.exit(1)

    results = calculate_nums_in_block(row_num=row_num,
                                      starting_from=starting_from,
                                      rows_in_block=rows_in_block,
                                      adding_each=adding_each,
                                      results_num=results_num)
    print(results)

def calculate_nums_in_block(row_num, starting_from, rows_in_block, adding_each, results_num):
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