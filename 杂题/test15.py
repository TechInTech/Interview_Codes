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
