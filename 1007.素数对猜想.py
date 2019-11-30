"""
让我们定义dn为：dn = pn+1 − pn，其中pi是第i个素数。显然有d1 = 1，且对于n>1有dn是偶数。
“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。

现给定任意正整数 N(<10^5) ，请计算不超过N的满足猜想的素数对的个数。

输入格式:
输入在一行给出正整数N。

输出格式:
在一行中输出不超过N的满足猜想的素数对的个数。

输入样例:
20
输出样例:
4
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


def twin_prime(n: int):
    if n <= 3:
        return False
    if prime(n):
        if prime(n-2):
            return True
    return False


if __name__ == '__main__':
    n = int(input())
    count = 0
    while n > 2:
        if twin_prime(n):
            count += 1
        n -= 1
    print(count)
