"""
设计函数求一元多项式的导数。（注：x​^n （n为整数）的一阶导数为 n x^n−1 。）

输入格式:
以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过 1000 的整数）。数字间以空格分隔。

输出格式:
以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，但结尾不能有多余空格。
注意“零多项式”的指数和系数都是 0，但是表示为 0 0。

输入样例:
3 4 -5 2 6 1 -2 0
输出样例:
12 3 -10 1 6 0
"""


def derivation(in_list: list):
    out_list = []
    l = len(in_list)
    if l == 0 or (l == 2 and int(in_list[-l + 1]) == 0):
        return '0 0'
    while l:
        if int(in_list[-l + 1]) == 0:
            l -= 2
        else:
            out_list.append(str(int(in_list[-l]) * int(in_list[-l+1])))
            out_list.append(str(int(in_list[-l+1]) - 1))
            l -= 2
    return ' '.join(out_list)


if __name__ == '__main__':
    in_list = str(input()).split()
    print(derivation(in_list))
