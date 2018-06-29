#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
大数相加
描述
两个长度超出常规整形变量上限的大数相加，请避免使用各语言内置大数处理库，如 Java.math.BigInteger 等。

输入
有 N 行测试数据，每一行有两个代表整数的字符串 a 和 b，长度超过百位。规定 a, b > 0。
测试结果可以用 linux 小工具 bc进行测试是否正确。

输出
返回表示结果整数的字符串。
"""


def solution(line):
    a, b = line.strip().split(' + ')
    if(len(a) - len(b) >= 0):
        l = '0' + a
        s = '0' + b
    elif(len(a) - len(b) < 0):
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


s = "9999000000000 + 1999999"
s1 = "0 + 0"
print solution(s)
print solution(s1)