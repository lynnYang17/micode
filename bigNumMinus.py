#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
大数相减
序号：#3 难度：有挑战  时间限制：1000ms  内存限制：100M
描述
两个长度超出常规整形变量上限的大数相减，请避免使用各语言内置大数处理库，如 Java.math.BigInteger 等。

输入
有 N 行测试数据，每一行有两个代表整数的字符串 a 和 b，长度超过百位。规定 a>=b，a, b > 0。
测试结果可以用 linux 小工具 bc进行测试是否正确。

输出
返回表示结果整数的字符串。
"""


def solution(line):
    a, b = line.strip().split(" - ")
    for i in range(len(a) - len(b)):
        b = '0' + b
    res = ''
    jiewei = 0
    for i in range(len(a) - 1, -1, -1):
        tempa = int(a[i])
        tempb = int(b[i])  # 字符串能相减？ASCII？什么可以直接相减得到int相减的数字字符？
        '''if tempa > tempb and jiewei ==0:
            res = str(tempa - tempb) + res
            jiewei = 0
        elif tempa > tempb and jiewei == 1:
            res = str(tempa - 1 - tempb) +res
            jiewei = 0
        elif tempa == tempb and jiewei == 0:
            res = '0' + res
            jiewei = 0
        elif tempa == tempb and jiewei == 1:
            res = str(tempa + 10 - 1 - tempb) + res
            jiewei = 1
        elif tempa < tempb and jiewei == 0:
            res = str(tempa + 10 - tempb) + res
            jiewei = 1
        elif tempa < tempb and jiewei == 1:
            res = str(tempa + 10 - 1 - tempb) + res
            jiewei = 1
        '''
        if tempa - tempb -jiewei >= 0:
            res = str(tempa - tempb -jiewei) + res
            jiewei = 0
        elif tempa - tempb -jiewei < 0:
            res = str(tempa + 10 - jiewei - tempb) + res
            jiewei = 1

    return res


s = "1200 - 999"
print str(int(solution(s)))
