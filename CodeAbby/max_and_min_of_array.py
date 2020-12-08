def main():
    items=list(map(int, input().split()))
    myMax=items[0]
    myMin=items[0]
    for i in items:
        if i>myMax:
            myMax=i
        if i<myMin:
            myMin=i
    print ('{} {}'.format(myMax, myMin))




if __name__=='__main__':
    main()





