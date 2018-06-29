#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
大数的加法运算与大小判断
序号：#19 难度：有挑战  时间限制：1000ms  内存限制：10M
描述
对于给定的算术表达式，按规则输出计算结果，仅包含加法和大小判断。

输入
一行字符串，为加号、大于、小于( + < > ) 连接的两个不限大小的非负整数。

输出
 当符号为 + 时, 计算两个数相加的和, 并以字符串格式返回；
 当符号为 < 时, 如果左数小于右数, 返回大写字母字符 Y, 否则返回大写字母字符 N；
 当符号为 > 时, 如果左数大于右数, 返回大写字母字符 Y, 否则返回大写字母字符 N。

!!!请同学们尽量使用算法来解决这个问题
"""


def solution(line):
    flag = ''
    if line.find('+') >= 0:
        a, b = line.strip().split('+')
        flag = '+'
    elif line.find('>') >= 0:
        a, b = line.strip().split('>')
        flag = '>'
    elif line.find('<') >= 0:
        a, b = line.strip().split('<')
        flag = '<'

    if flag == '+':
        if (len(a) - len(b) >= 0):
            l = '0' + a
            s = '0' + b
        elif (len(a) - len(b) < 0):
            l = '0' + b
            s = '0' + a
        else:
            return '0'

        res = ''
        for i in range(len(l) - len(s)):
            s = '0' + s
        jinwei = 0
        for i in range(len(l) - 1, -1, -1):
            templ = int(l[i])
            temps = int(s[i])
            if templ + temps + jinwei < 10:
                res = str(templ + temps + jinwei) + res
                jinwei = 0
            elif templ + temps + jinwei >= 10:
                res = str(templ + temps + jinwei - 10) + res
                jinwei = 1
        return str(int(res))
    elif len(a) > len(b):
        if flag == '>':
            return 'Y'
        elif flag == '<':
            return 'N'
    elif len(a) < len(b):
        if flag == '>':
            return 'N'
        elif flag == '<':
            return 'Y'
    elif len(a) == len(b):
        for i in range(len(a)):
            if int(a[i]) > int(b[i]):
                if flag == '>':
                    return 'Y'
                elif flag == '<':
                    return 'N'
            elif int(a[i]) < int(b[i]):
                if flag == '>':
                    return 'N'
                elif flag == '<':
                    return 'Y'
            elif int(a[i]) == int(b[i]):
                if i != len(a) - 1:
                    continue
                return 'N'


s = '972919822976663297>74058'
s1 = "0+0"
s2 = "798876108959508902791396730547>788499852767910683563323887278"
s3 = "582>582"
print solution(s)
print solution(s1)
print solution(s2)
print solution(s3)
