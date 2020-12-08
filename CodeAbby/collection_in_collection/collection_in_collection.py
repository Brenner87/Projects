import logging

def main():
    pass


def check_config(col, key, value):
    conf=col
    for i in key.split('.'):
        if not i:
            return False
        try:
            i = int(i)
        except ValueError:
            pass
        try:
            conf=conf[i]
        except KeyError:
            return False
    if conf != value:
        return False
    return True


def set_value(config, key, value):
    col = {}
    keys = key.split('.')
    for i in keys:
        col[i] = {}
        

        
        

if __name__ == '__main__':
    main()
