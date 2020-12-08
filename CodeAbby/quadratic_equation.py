from math import sqrt
import cmath

def main():
    unpacker = lambda x=0, y=0, z=0: (x, y, z)
    results = []
    n = int(input())
    for i in range(n):
        a, b, c = unpacker(*list(map(int, input().split(' '))))
        d = b ** 2 - 4 * a * c
        if d >= 0:
            x1 = str(round((-b + sqrt(d)) / (2 * a)))
            x2 = str(round((-b - sqrt(d)) / (2 * a)))
        else:
            x1 = str((-b + cmath.sqrt(d)) / (2 * a)).replace('(','').replace(')', '').replace('j', 'i')
            x2 = str((-b - cmath.sqrt(d)) / (2 * a)).replace('(','').replace(')', '').replace('j', 'i')
        results.append('{} {}'.format(x1, x2))
    print('; '.join(results))



if __name__ == '__main__':
    main()