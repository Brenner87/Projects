


try:
    f = open('test0s0df.py')
    if f.name =='test.py':
        raise Exception
except FileNotFoundError as error:
    print(error)
except Exception as error:
    print ('Wrong name!!!')
else:
    print (f.read())
    f.close()
finally:
    print("Executing finally")
    print("This is not the end")


