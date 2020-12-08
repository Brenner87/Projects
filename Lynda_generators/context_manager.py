from contextlib import contextmanager
from time import time

HEADER="this is the header \n"
FOOTER="\nthis is the footer \n"

def main():
    obj=Some_obj(5)
    print(obj.some_property)
    with simple_context_manager(obj):
        print (obj.some_property)
    print(obj.some_property)




    with new_log_file('logfile') as file:
        file.write('this is the body')


@contextmanager
def new_log_file(name):
    try:
        logname=name
        f=open(logname, 'w')
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print("logfile created")
        f.close()

@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property+=1
        yield
    finally:
        obj.some_property-=1


class Some_obj(object):
    def __init__(self, arg):
        self.some_property=arg


if __name__=='__main__':
    main()