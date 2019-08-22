# -*- coding：utf-8-*-
"""
# n, m 分别表示数字含有n位，和在m进制下。(n, m <= 100000)
# 这里令ls1,ls2分别为两个包含n个整数，采用空格隔开的输入，
# 每个整数都在0到m-1之间，每行第i个数表示的是当前数第i位上的数字。
# ~~~~~~~~~~~~~~~~~~~~~~~~~~ 思路 ~~~~~~~~~~~~~~~~~~~~~
## 首先遍历ls1的每个数，再遍历ls2的每个数字，保留两个数字之和对进制m取模的最大值，
## 保存在数组result中，同时删除ls2中与ls1中数字之和取模最大值时ls2中数字对应的值，
## 遍历完毕后，对result进行降序排序，输出结果
"""
import  sys

if __name__ == '__main__':
    # 候选人数
    n, m = map(int,input().strip().split())
    ls1 = list(map(int,sys.stdin.readline().strip().split()))
    ls2 = list(map(int,input().strip().split()))

    result = []

    for i in range(len(ls1)):
        max_val = 0
        index_ = i
        for j in range(len(ls2)):
            val = ls1[i] + ls2[j]
            mod_val = val % m
            if mod_val > max_val:
                max_val = mod_val
                index_ = j
        del ls2[index_]
        result.append(max_val)

    result = sorted(result, reverse=True)

    print(' '.join(map(str, result)))
