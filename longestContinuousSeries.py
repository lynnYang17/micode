#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
最长连续数列
序号：#4 难度：困难  时间限制：1000ms  内存限制：10M
描述
输入一个乱序的连续数列，输出其中最长连续数列长度，要求算法复杂度为  O(n)  。

输入
54,55,300,12,56

输出
3
"""


def solution(line):
    s = line.strip().split(',')
    ans = -1
    mapp = {}
    for i in s:
        temp = int(i)
        if mapp.has_key(temp - 1) and not mapp.has_key(temp + 1):
            mapp[temp] = mapp[temp - 1] + 1
            if mapp[temp] > ans:
                ans = mapp[temp]
            k = temp - 1
            while (mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k -= 1
        elif mapp.has_key(temp + 1) and not mapp.has_key(temp - 1):
            mapp[temp] = mapp[temp + 1] + 1
            if mapp[temp] > ans:
                ans = mapp[temp]
            k = temp + 1
            while (mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k += 1
        elif not mapp.has_key(temp + 1) and not mapp.has_key(temp - 1):
            mapp[temp] = 1
            if mapp[temp] > ans:
                ans = mapp[temp]
        elif mapp.has_key(temp + 1) and mapp.has_key(temp - 1):
            mapp[temp] = mapp[temp + 1] + mapp[temp - 1] + 1
            if mapp[temp] > ans:
                ans = mapp[temp]
            k = temp - 1
            while (mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k -= 1
            k = temp + 1
            while (mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k += 1
        # print temp, mapp[temp]

    return ans


s = "57,54,55,300,12,56"
print solution(s)