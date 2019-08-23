# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/8/12 8:32
# @Author  : Despicable Me
# @Email   : 
# @File    : 03_similary.py
# @Software: PyCharm
# @Explain :
"""
# 输入一个正数s，打印出所有和为s的连续正整数序列（至少含有两个数）。
# 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，
# 所以结果打印出这{1,2,3,4,5 }、{4,5,6}，{7,8}三个序列
"""

if __name__ == '__main__':
    s = int(input())
    if s < 3:
        print()
    else:
        i, j = 1, 2
        sum_s = i + j
        sequence = []
        while i < (s+1)//2 and i < j:
            if sum_s == s:
                sequence.append(list(range(i, j+1)))
                j += 1
                sum_s += j
            elif sum_s < s:
                j += 1
                sum_s += j
            else:
                sum_s -= i
                i += 1
        print(sequence)