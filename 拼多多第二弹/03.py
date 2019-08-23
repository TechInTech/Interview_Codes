# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/8/11 21:19
# @Author  : Despicable Me
# @Email   : 
# @File    : 03.py
# @Software: PyCharm
# @Explain :
"""
# 给定两个正整数n和s,去满足序列长度为n,序列元素和为s的递增数列的个数
"""


if __name__ == '__main__':
    n, s = map(int, input().split())

    pre = s // n
    # 如果
    for i in range(1, pre):
