import re


def test():
    str_get = str(input())
    count = str_get.count('AAS')
    result = re.split('[PT]', str_get)
    print(result, count)


if __name__ == '__main__':
    test()
