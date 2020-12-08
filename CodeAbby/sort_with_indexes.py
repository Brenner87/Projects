

def main():
    n = int(input())
    items = list(map(int, input().split(' ')))
    results = [str(items.index(i) + 1) for i in sorted(items)]
    print(' '.join(results))


if __name__ == '__main__':
    main()