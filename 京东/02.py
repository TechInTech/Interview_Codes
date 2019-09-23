# -*- coding:utf-8 -*-
def get_flag(n, m, local_index):
    lyst = [[0, 0], [0, m-1], [n-1, 0], [n-1, m-1]]
    max_val = []
    for item in lyst:
        max_val.append(abs(item[0] - local_index[0]) + abs(item[1] - local_index[1]))
    return max(max_val)

if __name__ == "__main__":
    T = int(input())
    i = 0
    while i < T:
        i += 1

        n, m = map(int, input().split())

        j = 0
        dot_count = 0
        jing_count = 0
        s_local = []

        while j < n:
            line = list(input())
            dot_count += line.count('.')
            jing_count += line.count('#')
            if 'S' in line:
                s_local.append([j, line.index('S')])
            j += 1

        flag = [False]*len(s_local)
        for item in range(len(s_local)):
            max_val = get_flag(n, m, s_local[item])
            if max_val <= dot_count + len(s_local) - 1:
                flag[item] = True

        if True in flag:
            print("Yes")
        else:
            print("No")
