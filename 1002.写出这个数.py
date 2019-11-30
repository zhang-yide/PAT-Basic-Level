"""
读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

输入格式：
每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10^100。

输出格式：
在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。

输入样例：
1234567890987654321123456789
输出样例：
yi san wu
"""


def print_number():
    num_pinyin = {'0': 'ling', '1': 'yi', '2': 'er', '3': 'san', '4': 'si',
                  '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu'}
    number = str(input())
    number_sum = 0
    result = []
    for num in number:
        number_sum += int(num)
    for num in str(number_sum):
        result.append(num_pinyin[num])
    print(' '.join(result))


if __name__ == '__main__':
    print_number()
