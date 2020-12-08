import sys
import re


def main():
    # file_name=sys.argv[1]
    file_name = 'file_for_names.txt'
    result=get_uniq_name(file_name)
    [print(i) for i in result]



def get_uniq_name(file_name):
    user = re.compile("^.*?Username\s*?=\s*?([\w/]+).*$")
    try:
        with open (file_name) as f:
            names={user.match(i).group(1) for i in f if user.match(i)}
            return sorted(names)
    except Exception as err:
        print('oops: {}'.format(err))
        return None


if __name__=='__main__':
    main()