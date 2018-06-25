#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
找出旋转有序数列的中间值
序号：#5 难度：一般  时间限制：1000ms  内存限制：10M
描述
给出一个有序数列随机旋转之后的数列，如原有序数列为：[0,1,2,4,5,6,7] ，旋转之后为[4,5,6,7,0,1,2]。
假定数列中无重复元素，且数列长度为奇数。
求出旋转数列的中间值。如数列[4,5,6,7,0,1,2]的中间值为4。

输入
4,5,6,7,0,1,2

输出
4
"""


# by yanglin
def solution(line):
    s = line.strip().split(',')
    flag = -1
    for i in range(len(s) - 1):#???
        if int(s[i]) > int(s[i + 1]):
            flag = i
    if flag == -1:
        return s[len(s)/2]
    if flag >= len(s)/2:
        return s[flag - (len(s) - 1)/2]
    if flag < len(s)/2:
        return s[flag + 1 + (len(s) - 1)/2]


a = "4,5,6,7,0,1,2"
s = "12,13,14,5,6,7,8,9,10"
print solution(a)
print solution(s)


'''
# by zhoujian
def solution(line):
    a = line.strip().split(',')
    flag = -1
    for i in range(len(a) - 1):
        if int(a[i + 1]) < int(a[i]):
            flag = i
    if flag == -1:
        return a[len(a)/2]
    elif flag == len(a)/2:
        return a[0]
    elif flag < len(a)/2:
        return a[(len(a) + 2*flag + 2)/2]
    elif flag > len(a)/2:
        return a[(flag - (len(a) - 1 - flag))/2]


s = "4,5,6,7,0,1,2"
print solution(s)
'''
