"""
给定一系列正整数，请按要求对数字进行分类，并输出以下 5 个数字：
A1 = 能被 5 整除的数字中所有偶数的和；
A2 = 将被 5 除后余 1 的数字按给出顺序进行交错求和，即计算 n1 −n2 + n3 −n4⋯；
A3 = 被 5 除后余 2 的数字的个数；
A4 = 被 5 除后余 3 的数字的平均数，精确到小数点后 1 位；
A5 = 被 5 除后余 4 的数字中最大数字。

输入格式：
每个输入包含 1 个测试用例。每个测试用例先给出一个不超过 1000 的正整数 N，
随后给出 N 个不超过 1000 的待分类的正整数。数字间以空格分隔。

输出格式：
对给定的 N 个正整数，按题目要求计算 A1 ~ A5
并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。
若其中某一类数字不存在，则在相应位置输出 N。

输入样例 1：
13 1 2 3 4 5 6 7 8 9 10 20 16 18
输出样例 1：
30 11 2 9.7 9
"""


def sort_num(num_list: list):
    N = int(num_list.pop(0))
    a1 = a2 = a3 = a4 = a5 = 0
    flag_a2 = 1
    exist_a2 = False
    count_a4 = 0
    for i in num_list:
        i = int(i)
        remainder = i % 5
        if remainder == 0:
            if i % 2 == 0:
                a1 += i
        elif remainder == 1:
            exist_a2 = True
            a2 += i * flag_a2
            flag_a2 *= -1
        elif remainder == 2:
            a3 += 1
        elif remainder == 3:
            a4 += i
            count_a4 += 1
        elif remainder == 4:
            if i > a5:
                a5 = i
    if count_a4:
        a4 = round(a4 / count_a4, 1)
    out_list = [
        str(a1) if a1 else 'N',
        str(a2) if exist_a2 else 'N',
        str(a3) if a3 else 'N',
        str(a4) if a4 else 'N',
        str(a5) if a5 else 'N'
    ]
    out_str = ' '.join(out_list)
    print(out_str)


if __name__ == '__main__':
    in_str = input()
    in_list = in_str.split()
    sort_num(in_list)

