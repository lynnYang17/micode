#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
第一个缺失正数
序号：#7 难度：有挑战  时间限制：1000ms  内存限制：10M
描述
给出一个无序的数列，找出其中缺失的第一个正数，要求复杂度为 O(n)
如：[1,2,0]，第一个缺失为3。
如：[3,4,-1,1]，第一个缺失为2。

输入
1,2,0

输出
3
"""


def solution(line):
    s = line.strip().split(',')
    mapp = {}
    for i in s:
        mapp[int(i)] = 1
    ans = 1
    while 1:
        if mapp.has_key(ans):
            ans += 1
        else:
            return ans


s = "1,2,0"
print solution(s)