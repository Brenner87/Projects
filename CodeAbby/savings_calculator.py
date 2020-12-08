
def main():
    results = []
    n = int(input())
    for i in range(n):
        amount, required, interest = list(map(int, input().split(' ')))
        year = 0
        while amount < required:
            amount *= 1 + (interest / 100)
            year += 1
        results.append(str(year))
    print(' '.join(results))

if __name__ == '__main__':
    main()