def main():
    running=calculate()
    running.output()

class calculate:
    def __init__(self):
        self.n=int(input())
        self.numbers=input().split()

    def weighted_sum(self,item):
        mysum=0
        for i in range(len(item)):
            mysum=mysum+(i+1)*int(item[i])
        return mysum

    def calculate_all(self):
        result=(self.weighted_sum(i) for i in self.numbers)
        return list(result)

    def output(self):
        print (' '.join(map(str, self.calculate_all())))

if __name__=='__main__':
    main()

