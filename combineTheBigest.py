#!/usr/bin/python
# -*- coding: UTF-8 -*=
"""
按序组合成最大的数
序号：#21 难度：困难  时间限制：1000ms  内存限制：10M
描述
给定两个数组，由数字 0-9 组成的，长度分别为 a 和 b，需要用 a、b 两个数组中的数字组合得到长度为 k （k <= a+b）的正整数，输出所有可能的组合中数值最大的一个（原同一数组中的数字顺序不能改变）

输入
a、b 数组中的数字间用 , 隔开，两个数组以及 k 之间用空格隔开，如：1,3,4,5,1,2 8,9,1 5，其中 a = [1,3,4,5,1,2]，b = [8,9,1]，k = 5

输出
长度为 k 的所有组合中数值最大的整数，如：95121

* 从 a 或 b 中取数的时候需保证 a，b 内部的顺序不变，如第一个数取到 b 中的 9，那么 b 中只有 1 可以后续取用；第二个数取到 a 中的 5，则 a 中还剩下 1,2 可以后续取用。
"""


def solution(line):
    a, b, k = line.strip().split(' ')
    A = a.split(',')
    B = b.split(',')
    k = int(k)
    ans = ''
    tempans = ''
    max_num_A = min(len(A), k)
    min_num_A = max(0, k - len(B))

    for i in range(min_num_A, max_num_A + 1):
        select_num_A = len(A) - i
        select_num_B = len(B) - k + i
        # print select_num_A, select_num_B
        # for A
        tempA = A
        cntA = 0
        for i in range(select_num_A):
            for j in range(len(tempA) - 1):
                if j + 1 >= len(tempA):
                    break
                if tempA[j] < tempA[j + 1]:
                    tempA = tempA[:j] + tempA[j + 1:]
                    cntA += 1
                    break
        # for B
        tempB = B
        cntB = 0
        for i in range(select_num_B):
            for j in range(len(tempB) - 1):
                if j + 1 >= len(tempB):
                    break
                if tempB[j] < tempB[j + 1]:
                    tempB = tempB[:j] + tempB[j + 1:]
                    cntB += 1
                    break

        if cntA < select_num_A:
            tempA = tempA[:len(tempA) - (select_num_A - cntA)]
        if cntB < select_num_B:
            # print len(tempB)-(select_num_B - cntB)
            tempB = tempB[:len(tempB) - (select_num_B - cntB)]
        # print cntA, select_num_A
        # print tempA
        # print cntB, select_num_B
        # print tempB
        # print len(tempA) + len(tempB)
        # break
        while 1:
            # print tempA
            # print tempB
            if len(tempA) + len(tempB) == 0:
                break
            if len(tempA) == 0:
                while len(tempB) > 0:
                    tempans += tempB[0]
                    tempB = tempB[1:]
            elif len(tempB) == 0:
                while len(tempA) > 0:
                    tempans += tempA[0]
                    tempA = tempA[1:]
            else:
                if tempA[0] > tempB[0]:
                    tempans += tempA[0]
                    tempA = tempA[1:]
                elif tempA[0] < tempB[0]:
                    tempans += tempB[0]
                    tempB = tempB[1:]
                elif tempA[0] == tempB[0]:
                    flagA = tempA[0]
                    flagB = tempB[0]
                    flag = 0
                    if len(tempA) == 1 and len(tempB) == 1:
                        flagA = tempA[0]
                        flagB = tempB[0]
                        flag = 0 if flagA >= flagB else 1

                    elif len(tempA) == 1 and len(tempB) > 1:
                        flagA = tempA[0]
                        for i in range(len(tempB) - 1):
                            if tempB[i] != tempB[i + 1]:
                                flagB = tempB[i + 1]
                                break
                        flag = 0 if flagA >= flagB else 1

                    elif len(tempA) > 1 and len(tempB) == 1:
                        flagB = tempB[0]
                        for i in range(len(tempA) - 1):
                            if tempA[i] != tempA[i + 1]:
                                flagA = tempA[i + 1]
                                break
                        flag = 0 if flagA >= flagB else 1

                    elif len(tempA) > 1 and len(tempB) > 1:
                        cnt = 0
                        while 1:
                            if cnt == len(tempA) or cnt == len(tempB):
                                break
                            else:
                                if tempA[cnt] > tempB[cnt]:
                                    flag = 0
                                    break
                                if tempA[cnt] < tempB[cnt]:
                                    flag = 1
                                    break
                                if tempA[cnt] == tempB[cnt]:
                                    cnt += 1
                    # print flag
                    if not flag:
                        tempans += tempA[0]
                        tempA = tempA[1:]
                    elif flag:
                        tempans += tempB[0]
                        tempB = tempB[1:]

            # print tempans
        # print tempans
        if tempans > ans:
            ans = tempans
        tempans = ''
    return ans


s = "1,3,4,5,1,2 8,9,1 5"
print solution(s)