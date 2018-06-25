#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
A + B
序号：#1 难度：一般  时间限制：2000ms  内存限制：128M
描述
和所有的 OJ 平台一样，第一题作为热身题，也是送分题：给出两个正整数 a 和 b，输出 a+b 的结果。

输入
一行数据包含两个正整数， a 和 b，空格分开。(a 和 b 保证小于 2^32)

输出
你的输出是对一行数据处理的结果，也即 a+b 的结果。
"""


def solution(line):
    a, b = line.strip().split(" ")
    return str(int(a) + int(b))


s = "13 48"
print solution(s)
