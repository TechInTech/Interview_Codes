# -*- coding：utf-8-*-
import sys

if __name__ == "__main__":
# """'the sky is            blue!'"""
    s = input().split()
    print(' '.join(s[-1::-1]))
    # 候选人数
    # n = int(sys.stdin.readline().strip())
    #print(sys.executable)

    # nums = n = 1000
    # for i in range(n-1, 0, -1):
    #     if nums%10 == 0:
    #         nums = nums//10
    #     if nums%10 != 0:
    #         num = str(nums)
    #         num = num[-1:-7:-1]
    #         nums = int(num[-1::-1])
    #     nums *= i
    #     print(nums)
    # print(len(str(nums)))

    # # n 个候选人信息
    # n_info = []
    # for i in range(n):
    #     # single = [m, m个指标]
    #     single_info = []
    #     m = int(sys.stdin.readline().strip())
    #     single_info.append(m)
    #     single_info.extend(list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
   #     n_info.append(single_info)

    # # 小娜的要求
    # # na_req = []
    # p = int(sys.stdin.readline().strip())
    # p_index = list(map(lambda x:int(x), sys.stdin.readline().strip().split()
    # na_req = dict(zip(p_index, [1]*p))

    # best_man = []
    # for each in n_info:
    #     num = 0
    #     for i in each[1::]:
    #         if i in na_req.keys():
    #             num += 1
    #     best_man.append([num, i+1])
    # best_man.sort()
    # print(best[0][1])
