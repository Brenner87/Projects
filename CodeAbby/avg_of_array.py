def main():
    n=int(input())
    result=[]
    for i in range(n):
        items=list(map(int, input().split()[:-1]))
        myAvg=sum(items)/len(items)
        result.append(str(round(myAvg)))
    print (' '.join(result))

def round(x):
    return int(x) + 1 if x-int(x) >= 0.5 else int(x)

if __name__=='__main__':
    main()