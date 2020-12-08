
def main():
    answer=[]
    for i in range(int(input())):
        dates = list(map(int, input().split()))
        instance=calculateDates(*dates)
        answer.append(instance.calcDate())
    print (' '.join(answer))





class calculateDates:
    def __init__(self,*args):
        self.args=args

    def getDiff(self):
        try:
            start=self.args[3]+self.args[2]*60+self.args[1]*60*60+self.args[0]*60*60*24
            end=self.args[-1]+self.args[-2]*60+self.args[-3]*60*60+self.args[-4]*60*60*24
        except Exception as err:
            print('Something went wrong: {}'.format(err))
            exit()
        return end-start

    def calcDate(self):
        diff=self.getDiff()
        secs=diff%60
        mins=diff//60%60
        hours=diff//60//60%24
        days=diff//60//60//24
        return "({} {} {} {})".format(days, hours, mins, secs)


if __name__ == '__main__':
    main()