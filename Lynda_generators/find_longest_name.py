def main():
    names=(name.strip().split(' ')[1] for name in open('names.txt'))
    lengths=((name, len(name)) for name in names)
    longest=max(lengths, key=lambda x:x[1])
    print(longest)



if __name__=='__main__':
    main()