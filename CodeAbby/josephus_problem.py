def main():
    num, step = list(map(int, input().split(' ')))
    seq = list(range(1, num + 1))
    count = 0
    while len(seq) != 1:
        for i in seq[:]:
            count += 1
            if count == step:
                seq.remove(i)
                count = 0
    print(range(num).index(seq[0]))

if __name__ == '__main__':
    main()