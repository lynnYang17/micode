#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
帮小学生排队
序号：#18 难度：有挑战  时间限制：1000ms  内存限制：10M
描述
用一个数组表示一群正在排队的小学生，每个小学生用一对整数来表示 [height, k], height 表示这个小学生的身高，k 表示这个小学生前面应该有 k 个人的身高 >= 他。

写一个算法，对给出的一组小学生计算出符合描述的正确排序。

输入
一行文本如：[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]，格式为 JSON（算法中可使用 JSON decode 得到数组）。

可以发现该序列不满足描述的条件，比如 [4,4] ：4 前面只有一个 7 大于 4。

输出
根据输入，重新排列数组，然后将符合条件的数组编码为 JSON 输出（不要有空格），如：[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]。
"""
import json


def solution(line):
    print line
    print type(line)
    s = json.loads(line)
    print type(s)
    print s[0]
    print type(s[0])
    print s[0][0]
    print type(s[0][0])
    return s


s = "[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]"
print solution(s)
