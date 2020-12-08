


def main():
    print(some_sub())
    print(some_sub(filename='something'))
    print(some_sub(table='firstTable'))
    print(some_sub(table='sometable', filename='somefile'))



def some_sub(**kwargs):
    output=kwargs.get('filename', 'lpo.db')
    table=kwargs.get('table', 'Weather')
    return output, table





if __name__=='__main__':
    main()
