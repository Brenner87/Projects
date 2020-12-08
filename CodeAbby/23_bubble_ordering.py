def main():
    in_data = list(map (int, input().split()))

    count = 0
    result = []
    temp = ''
    for i, item in enumerate(in_data):

        if in_data[i+1] == -1:
            result.append(temp or item)
            break

        if temp:
            item = temp

        if item > in_data[i+1]:
            result.append(in_data[i+1])
            temp = item
            count += 1
        else:
            result.append(item)
            temp = ''

    checksum = 0
    for i in result:
        checksum = (checksum + i)*113%10000007
    print(count, checksum)




if __name__ == '__main__':
    main()