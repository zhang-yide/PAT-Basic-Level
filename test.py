import time
import math


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        duration = stop_time - start_time
        print('用时:', duration * 3, 'ms')
    return deco


def test(l: list):
    return


@timer
def main():
    line1 = str(input())
    list1 = line1.split()
    N = int(list1[0])
    M = int(list1[1])
    line2 = str(input())
    list2 = line2.split()
    print(' '.join(list_move(list2, N, M)))


if __name__ == '__main__':
    while True:
        main()
