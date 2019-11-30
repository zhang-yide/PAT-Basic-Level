"""
“答案正确”是自动判题系统给出的最令人欢喜的回复。本题属于 PAT 的“答案正确”大派送 —— 只要读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”。

得到“答案正确”的条件是：
# 有且仅有'P', 'A', 'T'，三个字符。
1. 字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
# 'P'必须在'T'前，'P'和'T'之间只少有一个'A'。
2. 任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
# '**n1个A**P**n2个A**T**n3个A**'，其中 n3 = n1 * n2
3. 如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。

输入格式：
每个测试输入包含 1 个测试用例。第 1 行给出一个正整数 n (<10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。

输出格式：
每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。

输入样例：
8
PAT
PAAT
AAPATAA
AAPAATAAAA
xPATx
PT
Whatever
APAAATAA

输出样例：
YES
YES
YES
YES
NO
NO
NO
NO
"""
import re


def get_pass(string):
    # 判断是否只含有'P', 'T', 'A', 并判明'P', 'T'顺序
    count_p = 0
    count_t = 0
    for char in string:
        if char == 'P':
            if count_p != 0:
                return 'NO'
            else:
                count_p += 1
        elif char == 'T':
            if count_p != 1 or count_t != 0:  # 判断'T'是否在'P'后
                return 'NO'
            else:
                count_t += 1
        elif char == 'A':
            continue
        else:
            return 'NO'
    string_list = re.split('[PT]', string)

    # 判断含有共计两个'P'或'T'
    if len(string_list) != 3:
        return 'NO'
    # 判断在'**n1个A**P**n2个A**T**n3个A**'中，是否 n3 = n1 * n2，且n2 != 0
    else:
        n1 = string_list[0].count('A')
        n2 = string_list[1].count('A')
        n3 = string_list[2].count('A')
        if n2 != 0 and n3 == n1 * n2:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    count = int(input())
    for i in range(count):
        string = str(input())
        print(get_pass(string))
