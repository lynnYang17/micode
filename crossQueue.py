#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
交叉队列
序号：#6 难度：有挑战  时间限制：1000ms  内存限制：10M
描述
给出三个队列 s1，s2，s3 ，判断 s3 是否是由 s1 和 s2 交叉得来。
如：s1 为 aabcc ， s2 为 dbbca。
当 s3 为 aadbbcbcac 时，返回 true（即将 s1 拆成三部分： aa，bc，c 分别插入 s2 对应位置）
否则返回 false。

输入
aabcc,dbbca,aadbbcbcac

输出
true
"""
def solution(line):
    a, b, c = line.strip().split(',')
    ans = ''
    if len(a) + len(b) != len(c):
        ans = 'false'
        return ans
    if len(a) == 1 and len(b) == 1:
        if c == a + b or c == b + a:
            ans = 'true'
            return ans
        else:
            ans = 'false'
            return ans
    elif len(a) == 1 and len(b) != 1:
        usea = 0
        ib = 0
        flag = 0
        for i in range(len(c)):
            if c[i] == a and not usea:
                usea = 1
            elif c[i] == b[ib]:
                ib += 1
            else:
                flag = 1
                break
        if flag:
            ans = 'false'
            return ans
        else:
            ans = 'true'
            return ans

    if len(a) != 1 and len(b) == 1:
        useb = 0
        ia = 0
        flag = 0
        for i in range(len(c)):
            if c[i] == b and not useb:
                useb = 1
            elif c[i] == a[ia]:
                ia += 1
            else:
                flag = 1
                break
        if flag:
            ans = 'false'
            return ans
        else:
            ans = 'true'
            return ans

    else:
        j = 0
        while len(c) > 0:

            if len(a) > 1 and len(b) > 1 and a[0] != c[0] and b[0] != c[0]:
                return 'false'
            if len(a) > 1:
                for i in range(len(a) - 1, -1, -1):
                    if a[:i] == c[:i]:
                        a = a[i:]
                        c = c[i:]

            elif len(a) == 1 and len(c) == 1:
                if a == c:
                    return 'true'
                else:
                    return 'false'

            elif len(a) == 1 and len(c) > 1:
                if a == c[0]:
                    a = ''
                    c = c[1:]

            if len(b) > 1:
                for i in range(len(b) - 1, -1, -1):
                    if b[:i] == c[:i]:
                        b = b[i:]
                        c = c[i:]

            elif len(b) == 1 and len(c) == 1:
                if b == c:
                    return 'true'
                else:
                    return 'false'

            elif len(b) == 1 and len(c) > 1:
                if b == c[0]:
                    b = ''
                    c = c[1:]

        return 'true'
