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


def prime(n: int):
    if n == 2 or n == 3:
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    i = 5
    tmp = int(math.sqrt(n)+1)
    while i <= tmp:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        else:
            i += 6
    return True


def twin_prime(n: int):
    if n <= 3:
        return False
    if prime(n):
        if prime(n-2):
            return True
    return False


@timer
def main():
    n = int(input())
    count = 0
    while n > 2:
        if twin_prime(n):
            count += 1
        n -= 1
    print(count)


if __name__ == '__main__':
    main()
