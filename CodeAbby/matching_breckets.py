#!/usr/bin/python3

def main():
    n = int(input())
    items = [input() for i in range(n)]
    result = [str(analyze(i)) for i in items]
    print(' '.join(result))

def analyze(item):
    open = ['[', '{', '(', '<']
    close = [']', '}', ')', '>']
    open_stack=[]
    for i in item:
        if i in open:
            open_stack.append(i)
        if i in close:
            if not open_stack:
                return 0
            last = open_stack.pop()
            if last != open[close.index(i)]:
                return 0
    if len(open_stack) != 0:
        return 0
    return 1

if __name__ == '__main__':
    main()