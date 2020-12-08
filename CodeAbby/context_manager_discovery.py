



def main():
    with ContextM('before', 'after') as c:
        print('Im inside the block')
        c.middle = 1
        print(c.middle)
        print(c.aftermiddle)


class ContextM:
    def __init__(self, pre, post):
        self.pre = pre
        self.post = post

    def __enter__(self):
        print(self.pre)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print(self.post)
        else:
            print("Exception occured")
            raise ValueError("There is no such variable")




if __name__ == '__main__':
    main()