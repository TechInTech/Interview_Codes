# -*- coding: utf-8 -*-

import sys

MAX_LENGTH = 10

if __name__ == '__main__':

    # array_AB = []
    #
    # n = 2
    # while n > 0:
    #     array_str = sys.stdin.readline().strip().split(' ')
    #
    #     array_list = []
    #     for item in array_str:
    #         array_list.append(int(item))
    #     array_AB.append(array_list)
    #     n -= 1
    #
    # A_list = array_AB[0]
    # B_list = array_AB[1]
    # A_list = [7, 5, 6, 8, 10, 13, 15, 16]
    # B_list = [7, 2, 9, 10, 16, 8]
    A_list = [1, 2, 5, 3, 7]
    B_list = [2, 5, 5, 4, 9]

    max_val = -float('inf')
    exit_flag = False

    for i in range(len(A_list)):
        if i == 0:
            if A_list[i] >= A_list[i+1]:
                last = A_list[i + 1]
                for j in B_list:
                    if j < last:
                        exit_flag = True
                        if j >= max_val:
                            max_val = j
                    else:
                        continue
                break
        elif i == len(A_list) - 1:
            if A_list[i] <= A_list[i-1]:
                first = A_list[i-1]
                for j in B_list:
                    if j > first:
                        exit_flag = True
                        if j >= max_val:
                            max_val = j
                    else:
                        continue
                break
        elif ((A_list[i] < A_list[i+1] and A_list[i] <= A_list[i-1]) or (A_list[i] > A_list[i-1] and A_list[i] >= A_list[i+1])) and (A_list[i+1] - A_list[i-1]) > 1:
            first = A_list[i - 1]
            last = A_list[i + 1]
            for j in B_list:
                if first < j < last:
                    exit_flag = True
                    if j >= max_val:
                        max_val = j
                else:
                    continue
            break
        else:
            continue

    # max_val = -float('inf')
    # exit_flag = False
    # for j in B_list:
    #     if i == 0:
    #         last = A_list[i + 1]
    #         if j < last:
    #             exit_flag = True
    #             if j >= max_val:
    #                 max_val = j
    #         else:
    #             continue
    #     elif i == len(A_list) - 1:
    #         first = A_list[i-1]
    #         if j > first:
    #             exit_flag = True
    #             if j >= max_val:
    #                 max_val = j
    #         else:
    #             continue
    #     elif 0 < i < len(A_list) - 1:
    #         first = A_list[i - 1]
    #         last = A_list[i + 1]
    #         if first < j < last:
    #             exit_flag = True
    #             if j >= max_val:
    #                 max_val = j
    #         else:
    #             continue

    if exit_flag:
        del A_list[i]
        A_list.insert(i, max_val)
        print(A_list)
    else:
        print("NO")
