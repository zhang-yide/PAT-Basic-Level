"""
令 Pi表示第 i 个素数。现任给两个正整数 M≤N≤10^4，请输出 PM 到 PN 的所有素数。

输入格式：
输入在一行中给出 M 和 N，其间以空格分隔。

输出格式：
输出从 PM 到 PN 的所有素数，每 10 个数字占 1 行，其间以空格分隔，但行末不得有多余空格。

输入样例：
5 27
输出样例：
11 13 17 19 23 29 31 37 41 43
47 53 59 61 67 71 73 79 83 89
97 101 103
"""
import math


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


def print_prime():
    pass


if __name__ == '__main__':
    print_prime()
