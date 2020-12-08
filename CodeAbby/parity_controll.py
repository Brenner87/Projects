def main():
    my_str = list(map(int, input().split(' ')))
    print(''.join([convert(i) for i in my_str]))

def convert(item):
    digital = '{:08b}'.format(item)
    if digital.count('1') % 2 == 0:
        return chr(int(digital[1:], 2))
    return ''

if __name__ == '__main__':
    main()