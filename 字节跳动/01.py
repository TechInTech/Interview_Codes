# -*- coding:utf-8 -*-

if __name__ == "__main__":
    n = int(input())

    m = []
    i = 0
    while i < n:
        m.append(list(map(int, input().split())))
        i += 1

    Mo = [[]]
    for i in range(n):
        for j in range(i+1):
            if m[i][j] >= 3:
                for k in range(len(Mo)):
                    if i in Mo[k] or j in Mo[k]:
                        Mo[k].extend([i, j])
                        flag = False
                        break
                    else:
                        flag = True
                if flag:
                    Mo.append([i, j])
    del Mo[0]
    nums = len(Mo)
    length = 0
    for lyst in Mo:
        length += len(set(lyst))
    if length == n:
        print(nums)
    else:
        print(nums + n - length)

"""
3
0 4 0
4 0 0
0 0 0
# 2

3
0 4 0
4 0 6
0 6 0
# 1

4
0 4 0 0
4 0 5 0
0 5 0 4
0 0 4 0
# 1
"""
