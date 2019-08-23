# -*- coding:utf-8 -*-

import sys


if __name__ == '__main__':
    """
    print('Input two integers N and M: ')
    line1 = list(map(lambda x: int(x), sys.stdin.readline().strip().split(' ')))

    N, M = line1

    print('Input N positive integers: ')
    line_time = list(map(lambda x: int(x), sys.stdin.readline().strip().split(' ')))

    print('Input the dependency relationships of mission(M lines): ')
    line_M = sys.stdin.readlines()

    relation = []
    for line in line_M:
        relation.append(list(map(lambda x: int(x), line.strip().split(' '))))

    print(relation)
    """

    # 测试用例
    N, M = 7, 7
    line_time = [1, 3, 5, 2, 7, 6, 1]
    relation = [[1, 2], [1, 4], [2, 5], [3, 5], [3, 6], [4, 6], [4, 7]]
    
