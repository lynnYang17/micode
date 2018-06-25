#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
构建短字符串
序号：#11 难度：一般  时间限制：1000ms  内存限制：10M
描述
给定任意一个较短的子串，和另一个较长的字符串，判断短的字符串是否能够由长字符串中的字符构建出来，且长串中的每个字符只能用一次。

输入
一行数据包括一个较短的字符串和一个较长的字符串，用一个空格分隔，如：
ab aab
bb abc
aa cccc

输出
如果短的字符串可以由长字符串中的字符构建出来，返回字符串 “true”，否则返回字符串 "false"，注意返回字符串类型而不是布尔型。
"""


def solution(line):
    a, b = line.strip().split(' ')
    if len(a) == 1 and len(b) == 1:
        if a == b:
            return 'true'
        else:
            return 'false'
    elif len(a) == 1:
        for i in range(len(b)):
            if a == b[i]:
                return 'true'
        return 'false'
    else:
        mapp = {}
        for i in b:
            mapp[i] = 0

        for i in b:
            mapp[i] += 1

        for i in a:
            if mapp.has_key(i):
                if mapp[i] > 0:
                    mapp[i] -= 1
                else:
                    return 'false'
            else:
                return 'false'
        return 'true'


s = "mi zhizhqpoem"
print solution(s)