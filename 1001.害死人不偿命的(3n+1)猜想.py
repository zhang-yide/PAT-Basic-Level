"""
卡拉兹(Callatz)猜想：

对任何一个正整数 n，如果它是偶数，那么把它砍掉一半；如果它是奇数，那么把 (3n+1) 砍掉一半。
这样一直反复砍下去，最后一定在某一步得到 n=1。
我们今天的题目不是证明卡拉兹猜想，而是对给定的任一不超过 1000 的正整数 n，简单地数一下，需要多少步（砍几下）才能得到 n=1？

输入格式：
每个测试输入包含 1 个测试用例，即给出正整数 n 的值。

输出格式：
输出从 n 计算到 1 需要的步数。

输入样例：
3
输出样例：
5
"""


def count(n: int):
    count_time = 0
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int((3 * n + 1) / 2)
        count_time += 1
    return count_time


if __name__ == '__main__':
    n = int(input())
    count_time = count(n)
    print(count_time)
