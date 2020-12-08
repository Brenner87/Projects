def main():
    n=int(input())
    items=list(map(int, input().split()))
    result=0
    for i in items:
        result=(result+i)*113%10000007
    print(result)


if __name__=='__main__':
    main()