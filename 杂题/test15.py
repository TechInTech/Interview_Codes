# # # s = input()
# # # k = int(input())
# # #
# # # all_ = set(list(s))
# # # ele_ = []
# # # for i in all_:
# # #     count = s.count(i)
# # #     ele_.append(count)
# # #
# # # ele_ = sorted(ele_, reverse=True)
# # #
# # # while k > 0:
# # #     ele_[0] -= 1
# # #     k -= 1
# # #     ele_.sort(reverse=True)
# # #
# # # print(sum([i*i for i in ele_]))
# #
# #
# # N = int(input())
# #
# # def get_res(i, line, res):
# #     if sum(line) == N:
# #         line.append(i)
# #         res.append(line)
# #         line.pop()
# #         return res, line
# #     elif sum(line) > N:
# #         return res, line
# #
# #     line.append(i)
# #     res, line = get_res(i, line, res)
# #     i = N - sum(line)
# #     res, line = get_res(i, line, res)
# #
# #     return res, line
# #
# # res = []
# # for i in range(1, N+1):
# #     line = []
# #     res, line = get_res(i, line, res)
# #
# # for item in res:
# #     if len(item) == 1:
# #         print(item[0])
# #     else:
# #         print("+".join(map(str, item)))
#
# if __name__ == "__main__":
#     n = int(input())
#     nums = list(input().split())
#     res = []
#     for item in nums:
#         lyst = sorted(list(map(int, item)))
#         res.append(int("".join(list(map(str,lyst)))))
#     res.sort()
#     print(res[-1])
# -*-coding:utf-8 -*-
# import re
# if __name__ == "__main__":
#
#     s = input()
#     chi_str = ''.join(re.findall('[\u4e00-\u9afa5]',s))
#     alp_str = ''.join(re.findall(r'[A-Za-z]',s))
#     num_str = re.sub("\D", "", s)
#     l1 = len(chi_str)
#     l2 = len(alp_str)
#     l3 = len(num_str)
#     l4 = len(s) - l1 - l2 - l3
#     print("汉字个数:%d,字母个数:%d,数字个数:%d,其它字符个数:%d,数据中纯文本为:%s"%(l1,l2,l3,l4,chi_str))


# if __name__ == "__main__":
#     s = input().split()
#     ele_score = []
#     for item in s:
#         name_score = item.split(":")
#         name_score[1] = int(name_score[1])
#         ele_score.append(name_score)
#     n = len(ele_score)
#     while n > 1:
#         i = 1
#         while i < n:
#             if ele_score[i][1] < ele_score[i-1][1]:
#                 ele_score[i], ele_score[i-1] = ele_score[i-1], ele_score[i]
#             i += 1
#         n -= 1
#     ele_score.reverse()
#     for item in ele_score:
#         print(item[0]+":"+str(item[1]), end=" ")
