

def main():
    result = []
    n = int(input())
    for i in range(n):
        num, my_str = input().split(' ')
        my_str = my_str[int(num):] + my_str[:int(num)]
        result.append(my_str)
    print(' '.join(result))

    assert ' '.join(result) == 'iuerwcoxguiurfka asgorouwxyoayuonu bygewewfivbaccqjjnsfi cfvgavisyzobhoggpgmmuj qhsxhiyzazvcadigspdcoce rhvtefaxecyuoaubnea apggliuqcfwulug tautxqtnbwevbbuuqdcuues ueeuachteugumacoqgn bzgdaaoxdrupibueg joxxmioifuneyirohtllzmbv zqazpfarbuhkyyceeedd sgavkftdyaiiqnzcpvjanju'


if __name__ == '__main__':
    main()