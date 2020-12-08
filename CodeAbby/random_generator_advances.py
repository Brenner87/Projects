
def main():
    n = int(input())
    results = []
    for i in range(n):
        data = map(int, input().split(' '))
        results.append(calculate(list(data)))
    print(' '.join(results))



def calculate(data):
    a,c,m,value,item_num = data
    for i in range(item_num):
        value = (a * value + c) % m
    return str(value)

if __name__ == '__main__':
    main()