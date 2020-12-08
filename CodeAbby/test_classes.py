

def main():
    MyClass().printVar()
    k={1:2, 2:3, 3:4}
    print(k.get(4))

    system=None
    env='abc'
    pattern = '{}.{}'.format(system or '', env)
    
    print(pattern)


class MyClass:
    VAR='123'

    def __init__(self):
        pass
        print(getattr(self, 'VAR'))

    def printVar(self):
        print(self.VAR)


if __name__ == '__main__':
    main()