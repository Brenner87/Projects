
def main():
    n = int(input())
    results = [check_iterations(i) for i in input().split(' ')]
    print(' '.join(results))

def check_iterations(num):
    items = []
    items.append(num)
    while True:
        num = '{:08d}'.format(int(num) * int(num))[2:-2]
        if num in items:
            return str(len(items))
        items.append(num)

if __name__ == '__main__':
    main()