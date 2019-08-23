# -*- coding: utf-8 -*-

import sys
from itertools import permutations

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = tuple([int(item) for item in sys.stdin.readline().strip().split()])
    if n == 1:
        print(line[0])
    else:
        array = sorted(list(permutations(list(range(1, n+1)), n)))
        index_ = array.index(line)
        array_search = [i for i in array[-(index_ + 1)]]
        for i in array_search:
            print(i, end=' ')
