import collections

def main():
    results = []
    conditions = collections.OrderedDict([
        ('under', 18.5),
        ('normal', 25.0),
        ('over', 30.0),
        ('obese', 10000000000)
    ])
    n = int(input())
    for i in range (n):
        params = list(map(float, input().split(' ')))
        w_ind = params[0]/(params[1])**2
        res = next(key for key, value in conditions.items() if w_ind < value)
        results.append(res)

    print(' '.join(results))


if __name__ == '__main__':
    main()