#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
#******************************开始写代码******************************


def  find_longest_num_str(input):
    if not input:
        return None
    else:
        lyst = []
        for i in range(len(input)-1):
            if input[i] >= '0' and input[i] <= '9':
                for j in range(i, len(input)):
                    if input[j] >= '0' and input[j] <= '9':
                        lyst.append((j-i+1,input[i:j+1]))
                    else:
                        break
        lyst.sort(reverse=True)
        return lyst[0]
#******************************结束写代码******************************


try:
    _input = input()
except:
    _input = None


res = find_longest_num_str(_input)

if not res:
    print('0/' + "\n")
else:
    l1 = res[0]
    l2 = res[1]
    print( "%d/%s\n"% (l1, l2))
