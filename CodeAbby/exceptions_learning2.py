
def main():
    exc=ExcLearn()
    exc.calculate()
    exc.writeToFile('somefile.txt')




class ExcLearn(object):
    def __init__(self):
        while True:
            try:
                self.a=float(input("Enter a: "))
                self.b=float(input("Enter b: "))
            except (ValueError, TypeError) as e:
                print("ERROR: " + str(e))
            else: break

    def calculate (self):
        try:
            self.result=self.a/self.b
        except (ZeroDivisionError, ValueError, TypeError) as e:
            print("ERROR: " + str(e))

    def writeToFile(self, filename):
        if not hasattr(self, 'result'): return
        try:
            fh=open(filename, 'a')
            fh.write('{0} / {1} == {2}\n'.format(self.a, self.b, self.result))
        except Exception as e:
            print ('ERROR: ' + str(e))
        finally:
            fh.close()



if __name__=="__main__":
    main()