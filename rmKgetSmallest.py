#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
移除 K 位得到最小值
序号：#9 难度：困难  时间限制：500ms  内存限制：10M
描述
有一行由正数组成的数字字符串，移除其中的 K 个数，使剩下的数字是所有可能中最小的。

假设：
 字符串的长度一定大于等于 K
 字符串不会以 0 开头

输入
一行由正整数组成的数字字符串，和一个正整数 K，两个数据由英文逗号隔开，如：1432219,3。

输出
移除 K 位后可能的最小的数字字符串。
如 1432219 移除 4, 3, 2 这 3 个数字后得到 1219，为所有可能中的最小值。
"""


def solution(line):
    n, k = line.strip().split(',')
    k = int(k)
    cnt = 0
    for i in range(k):
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                n = n[:i] + n[i + 1:]
                cnt += 1
                break
    while n[0] == '0' and len(n) != 1:
        n = n[1:]
    n = n[:len(n) + cnt - k]
    if len(n) == 0:
        return 0
    return n


s = "1432219,3"
print solution(s)
