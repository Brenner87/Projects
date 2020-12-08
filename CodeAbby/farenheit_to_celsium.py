def main():
    data=temperature()
    data.inputData()
    data.calculate()
    data.printData()




class temperature (object):

    def __init__(self):
        self.result=[]

    def calculate(self):
        for far in self.in_data[1:]:
            cel = ((float(far) + 40) / 1.8) - 40
            res = int(cel + 0.5) if cel >= 0 else int(cel - 0.5)
            self.result.append(str(res))

    def __str__(self):
        return ' '.join(self.result)

    def outputData(self):
        return ' '.join(self.result)

    def inputData(self):
        self.in_data=input().split()

    def printData(self):
        print(' '.join(self.result))




if __name__=='__main__':
    main()