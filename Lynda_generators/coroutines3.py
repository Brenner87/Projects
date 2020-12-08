from coroutines import coroutine_decorator


def main():
   pass

@coroutine_decorator
def router():
    try:
        while True:
            line=yield
            (first, last)=line.split(' ')
            fnames.send(first)
            lnames.send(last.strip())
    except GeneratorExit:
        fnames.close()
        lnames.close()


@coroutine_decorator
def file_write(filename):
    try:
        with open(filename, 'a') as file:
            while True:
                line=yield
                file.write(line+'\n')
    except GeneratorExit:
        file.close()


if __name__=='__main__':
    main()
    fnames = file_write('first_names.txt')
    lnames = file_write('last_names.txt')
    router = router()
    for name in open('names.txt'):
        router.send(name)
    router.close()