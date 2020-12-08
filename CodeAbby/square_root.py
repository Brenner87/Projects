def main():
    number=int(input())
    output=[]
    for i in range(number):
        x,n=map(int, input().split())
        r=1
        for j in range(n):
            r=(r+x/r)/2
        output.append((round(r,11)))
    print (' '.join(map(str, output)))





if __name__=='__main__':
    main()

