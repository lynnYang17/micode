#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
找出可能的合的组合
序号：#12 难度：有挑战  时间限制：1000ms  内存限制：10M
描述
给出一组不重复的正整数，从这组数中找出所有可能的组合使其加合等于一个目标正整数 N，如：

一组数为 1, 2, 3，目标数为 4，那么可能的加合组合为：
1, 1, 1, 1
1, 1, 2
1, 2, 1
1, 3
2, 1, 1
2, 2
3, 1
注意相同的组合数字顺序不同也算一种，所以这个例子的结果是 7 种。

输入
一组不重复的正整数（, 隔开）以及目标正整数（与数组用空格隔开）

输出
所有可能的加合等于目标正整数 N 的组合种数
"""


def solution(line):
    a, b = line.strip().split(' ')
    a = a.strip().split(',')
    b = int(b)
    c = []
    for i in a:
        c.append(int(i))
    ans = 0
    while 1:
        tempa = c[0]
        c = c[1:]
        for i in a:
            if tempa + int(i) < b:
                c.append(tempa + int(i))
            elif tempa + int(i) == b:
                ans += 1
            else:
                break

        if len(c) == 0:
            return ans


s = "1,2,3 4"
print solution(s)