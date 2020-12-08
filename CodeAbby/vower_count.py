def main():
    n = int(input())
    items = [input() for i in range(n)]
    result = [str(analyze(i)) for i in items]
    print(' '.join(result))

def analyze(string):
    vowers = ['a', 'o', 'e', 'y', 'i', 'u']
    count = 0
    for i in string.lower():
        if i in vowers:
            count += 1
    return count


if __name__ == '__main__':
    main()