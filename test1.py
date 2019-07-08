# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here
    a = line.strip().split(',')
    t = [0]
    value = 0
    for i in a:
        t.append(int(i))
        value += int(i)
    if value%2 == 1:
        return 'false'
    value = int(value/2)
    t = np.array(t)
    bag = [[] for i in range(len(t))]
    for i in range((len(t))):
        for j in range(value+1):
            bag[i].append(0)
    for i in range(1, len(t)):
        for j in range(1, value+1):
            if j < t[i]:
                bag[i][j] = bag[i-1][j]
            else:
                bag[i][j] = max(bag[i-1][j], bag[i-1][j-t[i]]+t[i])
    if bag[len(t)-1][value] == value:
        return 'true'
    else:
        return 'false'
    # return 'your_answer'
