import re


def main():
    # #formula = '100/600'
    # formula = '100'
    # amount = 260
    # costs = [0.90, 1.67, 6.93]
    # a = calculate(formula, amount, costs)
    # print(a)


    reMatch('1341/4324')
    reMatch('134df1/4324')
    reMatch('4324/1')

def reMatch(value):
    expr = re.compile(r'^(\d+/?)*\d$')
    if not expr.fullmatch(value):
        print ("BAAAAAAD")
    else:
        print('OK')


def calculate(formula, amount, rates):
    costs = [k for k in [i.rate_id.rate, i.rate_id.rate_1, i.rate_id.rate_2, i.rate_id.rate_3] if k]
    formula = i.rate_id.formula
    total = 0
    if len(rates[1:]) != len(formula.split('/')):
        raise Exception('')
    if formula:
        args = [int(i) for i in formula.split('/')]
        for i in reversed(args):
            diff = amount - i
            if diff > 0:
                amount -= diff
                total += rates.pop(-1)*diff
    total += amount*rates[0]
    return total




if __name__ == '__main__':
    main()
