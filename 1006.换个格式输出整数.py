"""
让我们用字母 B 来表示“百”、字母 S 表示“十”，用 12...n 来表示不为零的个位数字 n（<10），
换个格式来输出任一个不超过 3 位的正整数。
例如 234 应该被输出为 BBSSS1234，因为它有 2 个“百”、3 个“十”、以及个位的 4。

输入格式：
每个测试输入包含 1 个测试用例，给出正整数 n（<1000）。

输出格式：
每个测试用例的输出占一行，用规定的格式输出 n。

输入样例 1：
234
输出样例 1：
BBSSS1234
"""


def change_num_model(n: str):
    new_list = [['', '1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789'], 'S', 'B']
    n_list = list(n)
    len_n = len(n_list)
    result = []
    while len_n != 0:
        if len_n == 1:
            result.append(new_list[0][int(n_list[-len_n])])
            len_n -= 1
        else:
            result.append(new_list[len_n-1] * int(n_list[-len_n]))
            len_n -= 1
    result = ''.join(result)
    print(result)


if __name__ == '__main__':
    n = str(input())
    change_num_model(n)
