def main():
    m, n = map(int, input().split(' '))
    item = list(map(int, input().split(' ')))
    res = {}
    for i in range(1,n+1):
        found = [k for k in item if k == i]
        res[i]=len(found)
    result = ' '.join(map(str, res.values()))
    print(result)



if __name__ == '__main__':
    main()