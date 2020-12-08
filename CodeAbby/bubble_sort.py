
def main():
    n = int(input())
    items = list(map(int, input().split(' ')))
    total_swaps = 0
    total_pass = 1
    while True:
        k = total_swaps
        for n, i in enumerate(items):
            if n == 0:
                continue
            if items[n] < items[n-1]:
                total_swaps += 1
                t = items[n-1]
                items[n-1] = items[n]
                items[n] = t
        if k == total_swaps:
            break
        else:
            total_pass += 1

    print('{} {}'.format(total_pass, total_swaps))






if __name__ == '__main__':
    main()