def main():


    #c=coroutine_example()
    #c.__next__()


    c=counter('California')
    #c.__next__()
    print(c.send('Cali'))
    print(c.send('nia'))
    print (c.send('hawai'))
    print(c.send(1234))




def coroutine_example():
    while True:
        x=yield
        #do something with x
        print(x)



def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        cr=func(*args, **kwargs)
        cr.__next__()
        return cr
    return wrap



@coroutine_decorator
def counter(string):
    count=0
    try:
        while True:
            item=yield
            if isinstance(item,str):
                if item in string:
                    count+=1
                    print(item)
                else:
                    print('No Match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)




if __name__=='__main__':
    main()
