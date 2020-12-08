def main():
    running=calculate()
    running.output()

class calculate:
    def __init__(self):
        self.expression = ''
        while True:
            item=input()
            self.expression=str(eval(self.expression+item))
            if '%' in item:
                break

    def output(self):
        print (self.expression)

if __name__=='__main__':
    main()

