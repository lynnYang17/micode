#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
出现频率最高的前 K 个元素
序号：#13 难度：有挑战  时间限制：1000ms  内存限制：10M
描述
有一个不为空且仅包含正整数的数组，找出其中出现频率最高的前 K 个数，时间复杂度必须在 O(n log n) 以内。

输入
一行数据包括两部分，一个正整数数组（数字间 ',' 分隔）和一个正整数 K （1 ≤ K ≤ 数组长度），数组和 K 之间有一个空格。

输出
输出包含前 K 个出现频率最高的数，用 ', ' 分隔，保证升序排列。
"""


def solution(line):
    t, k = line.strip().split(' ')
    s = t.strip().split(',')
    mapp = {}
    value = []
    res = []
    for i in s:
        mapp[i] = 0
    for i in s:
        mapp[i] += 1
    print mapp
    #mapp = sorted(mapp.items(), key=lambda d: d[1], reverse=True)
    l = sorted(mapp.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    print l
    l = l[:int(k)]
    print l
    l = sorted(l, key=lambda d: d[0])
    print l
    res = ''
    for i in range(len(l)):
        #res += l[i][0] + ',' if i != len(l) - 1 else l[i][0]
        if i != len(l) - 1:
            res += l[i][0] + ','
        else:
            res += l[i][0]
    return res


s = "1,1,1,2,2,3 2"
print solution(s)
