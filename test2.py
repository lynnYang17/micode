# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here
    n, i = line.strip().split(',')
    n = int(n)
    i = int(i)
    up = 1
    down = 1
    for k in range(i-1):
        down = down*k
    for k in range(n, n+i-1):
        up = up*k
    return up/down
    # return 'your_answer'
