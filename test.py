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


#s = "4,5,6,7,0,1,2"
s = "12,13,14,5,6,7,8,9,10"
print solution(s)


'''def solution(line):
    a = int(line)
    b = []
    b.append(1)
    b.append(2)
    for i in range(2, a):
        b.append(int(b[i - 1]) + int(b[i - 2]))
    return b[a - 1]


s = "50"
print solution(s)

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


s = "3,4,-1,1"
print solution(s)




def sol(line):
    s = line.strip().split(',')
    ans = -1
    mapp = {}  # mapp = dict() 定义字典类型mapp
    for i in s:
        temp = int(i)
        # map[i] 代表当前key值为i的时候，数列中元素所能组成的最长连续串的长度
        if mapp.has_key(temp - 1) and not mapp.has_key(temp + 1):
            mapp[temp] = mapp[temp-1] + 1
            if mapp[temp]>ans:
                ans = mapp[temp]
            k = temp-1
            while(mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k -= 1
        elif mapp.has_key(temp + 1) and not mapp.has_key(temp - 1):
            mapp[temp] = mapp[temp+1] + 1
            if mapp[temp]>ans:
                ans = mapp[temp]
            k = temp+1
            while(mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k += 1
        elif not mapp.has_key(temp + 1) and not mapp.has_key(temp - 1):
            mapp[temp] = 1
            if mapp[temp]>ans:
                ans = mapp[temp]
        elif mapp.has_key(temp + 1) and mapp.has_key(temp - 1):
            mapp[temp] = mapp[temp+1] + mapp[temp-1] + 1
            if mapp[temp]>ans:
                ans = mapp[temp]
            k = temp-1
            while(mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k -= 1
            k = temp+1
            while(mapp.has_key(k)):
                mapp[k] = mapp[temp]
                k += 1
        #print temp, mapp[temp]

    return ans


s = '54,55,200,56'
print sol(s)

def sol(line):
    a, b = line.strip().split(' - ')
    print a
    for i in range(len(a) - len(b)):
        b = '0' + b
    print b
    ans = ''
    jiewei = 0
    for i in range(len(a) - 1, -1, -1):
        tempa = int(a[i])
        tempb = int(b[i])
        if tempa > tempb and jiewei == 0:
            ans = str(tempa - tempb) + ans
            jiewei = 0
        elif tempa > tempb and jiewei == 1:
            ans = str(tempa - 1 - tempb) + ans
            jiewei = 0
        elif tempa == tempb and jiewei == 0:
            ans = str(tempa - tempb) + ans
            jiewei = 0
        elif tempa == tempb and jiewei == 1:
            ans = str(tempa + 10 - 1 - tempb) + ans
            jiewei = 1
        elif tempa < tempb and jiewei == 0:
            ans = str(tempa + 10 - tempb) + ans
            jiewei = 1
        elif tempa < tempb and jiewei == 1:
            ans = str(tempa + 10 - 1 - tempb) + ans
            jiewei = 1

    return ans


s = '76 - 76'
print sol(s)


line = int(input())
ans = []
for i in range(line):
    s=raw_input().split()
    ans.append(int(s[0]) + int(s[1]))
for i in ans:
    print i

s = '1 2'
a, b = s.split(' ')

# 10 20 30 10 20 
ans = 10   s[0]
ans ^= s[1]  # 10 20 10 

ans ^= s[2]

ans
'''