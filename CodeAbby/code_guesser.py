
def main():
    guesses = {}
    n = int(input())
    for i in range(n):
        num, guessed = input().split(' ')
        guesses[guessed] = guesses.get(guessed, []) + [num]
    for i in range(10000):
        val = "{0:0=4d}".format(i)
        for n, items in guesses.items():
            found = check(items, val, int(n))
            if not found:
                break
        if found:
            print(val)
            break

def check(items, val, n):
    for item in items:
        k = 0
        for pos in range(len(val)):
            if val[pos] == item[pos]:
                k += 1
        if k != n:
            return False
    return True


if __name__ == '__main__':
    main()