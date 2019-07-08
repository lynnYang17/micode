# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here
    a = line.strip().split(',')
    cnt = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == 10 or abs(a[i] - a[j]) == 10:
                cnt += 1
    return cnt

            
    # return 'your_answer'
