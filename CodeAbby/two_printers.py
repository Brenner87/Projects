import math

def main():
    n = int(input())
    results = []
    for k in range(n):
        data = [i for i in map(int, input().split(' '))]
        results.append(calculate(data))
    print(' '.join(results))


def calculate(input):
    x,y,n = input
    #return str(min((math.ceil((max((x, y)) / float(x + y)) * n) * min((x, y)),
    #     math.ceil((min((x, y)) / float(x + y)) * n) * max((x, y)))))


    #return str(math.ceil(n/(1/x+1/y)))
    return str(math.ceil(n*y/(x+y))*x)


if __name__ == '__main__':
    main()