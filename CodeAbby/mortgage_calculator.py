
def main():
    loan, interest, time = list(map(int, input().split(' ')))

    k = 1 + interest / 100 / 12
    #payment = loan * k ** time * (1 - k) / (1 - k ** (time ))
    payment = 0
    while calculate(payment, time, interest, loan) > 0:
        payment += 1
    print(round(payment))


def calculate(payment, time, interest, loan):
    total = loan
    for i in range(1, time + 1):
        total += total * interest / 12 / 100 - payment
    return total

if __name__ == '__main__':
    main()