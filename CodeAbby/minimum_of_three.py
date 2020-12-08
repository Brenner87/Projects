#a=input().split()
#result=[]
#for i in range(int(a)):
#    row=input().split()
#    #min=row[0]
#    (min=j if j<min for j in row)
#    result.append(min)
#print (*result)


def main():
    myNumbers = Numbers()
    myNumbers.minOfThree()
    print(myNumbers)

class Numbers(object):
    def __init__(self):
        self.itemNum = int(input())
        self.result=[]

    def minOfThree(self):
        for i in range(self.itemNum):
            row = input().split()
            self.result.append(min(*row))


    def __str__(self):
        return (' ').join(self.result)

if __name__ == '__main__':
    main()