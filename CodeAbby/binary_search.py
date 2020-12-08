import math

def main():
    result = []
    n = int(input())
    precission = 1e-7
    for i in range(n):
        a, b, c, d = list(map(float, input().split(' ')))
        left, right = 0, 100
        while left <= right:
            middle = ((left + right) / 2)
            res = a * middle + b * math.sqrt(middle**3) - c * math.exp(-middle / 50) -d
            #print(left, right, middle, res)
            if math.isclose(res, 0, abs_tol=precission):
                result.append('{:.7f}'.format(middle))
                break
            if res < round(0, 7):
                left = middle + precission*0.01
            else:
                right = middle - precission*0.01
    print(' '.join(result))

if __name__ == '__main__':
    main()