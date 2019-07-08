#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
有 N⋅M 的一个矩阵，小米兔今天很开心，从矩阵左上角的第一个位置开始顺时针从外向里走，很快就走遍了所有的位置，可是小米兔想知道自己走过的轨迹，你能告诉小米兔它走过的轨迹吗？
（输出一个字符串，由小米兔走过的位置的值组成，用空格分隔。）

单组输入。

第 1 行是 2 个整数，分别代表 NN 和 MM 的值;
第 2 ~ NN + 1 行，表示 N⋅M 的矩阵中的每一行。

输入：
3 3
1 2 3
4 5 6
7 8 9

输出：
1 2 3 6 9 8 7 4 5

"""
import sys


def solution(m, n, s):
    up = 1
    bottom = m - 1
    left = 0
    right = n - 1

    ret = []
    flag = 0
    # 0 : from left to right
    # 1 : from up to bottom
    # 2 : from right to left
    # 3 : from bottom to up

    i = 0
    j = 0
    while len(ret) < m*n:
        # handle flag 0
        if flag == 0:
            ret.append(s[i][j])
            j += 1
            if j == right:
                flag = 1
                right -= 1
        # handle flag 1
        elif flag == 1:
            ret.append(s[i][j])
            i += 1
            if i == bottom:
                flag = 2
                bottom -= 1
        # handle flag 2
        elif flag == 2:
            ret.append(s[i][j])
            j -= 1
            if j == left:
                flag = 3
                left += 1
        # handle flag 3
        elif flag == 3:
            ret.append(s[i][j])
            i -= 1
            if i == up:
                flag = 0
                up += 1

    return ret


'''def solution(m, n, s):
    up = 1
    bottom = m - 1
    left = 0
    right = n - 1

    index = 0
    ret = []
    while index < m * n:
        # handle right
        i = 0
        j = 0
        while j <= right:
            ret.append(s[i][j])
            j = j + 1
            # print('i1: ' + str(i))
            print('j1: ' + str(j))
        j = j - 1
        right = right - 1
        # handle bottom
        while i < bottom:
            i = i + 1
            ret.append(s[i][j])
            print('i2: ' + str(i))
        bottom = bottom - 1
        # handle left
        while j >= left:
            j = j - 1
            ret.append(s[i][j])
            print('j3: ' + str(j))
        left = left + 1
        j = j + 1
        # handle up
        print('jjjjjj: ' + str(j))
        while i > up:
            i = i - 1
            ret.append(s[i][j])
            print('ijijijijijijijij: ' + str(s[i][j]))
            print('i4: ' + str(i))
        up = up + 1

        index = index + 1

    return ret
'''

m = 3
n = 3
s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution(m, n, s))


