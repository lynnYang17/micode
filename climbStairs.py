#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
爬楼梯
序号：#10 难度：一般  时间限制：1000ms  内存限制：10M
描述
在你面前有一个n阶的楼梯，你一步只能上1阶或2阶。
请问计算出你可以采用多少种不同的方式爬完这个楼梯。

输入
一个正整数，表示这个楼梯一共有多少阶

输出
一个正整数，表示有多少种不同的方式爬完这个楼梯
"""


def solution(line):
    n = line.strip()
    n = int(line)
    a = []
    a.append(1)
    a.append(2)
    for i in range(2, n):
        a.append(a[i - 2] + a[i - 1])
    return a[n - 1]


s = "50"
print solution(s)