# ls1 = list(map(int, input().split()))
#
# ls2 = list(map(int, input().split()))
#
# ls = [ls1, ls2]
#
# for item in ls:
#     sums = 0
#     for i in set(item):
#         n = item.count(i)
#         sums += n*n
#     print(sums-2)
# ls = input().split()
#
# ls[-1] = ls[-1][0:len(ls[-1])-1]
#
# ls.reverse()
#
# ls[-1] = ls[-1]+'.'
#
# print(" ".join(ls))
#
# s1 = input()
# s2 = input()
#
# def get_res(s1, s2):
#     n, m = len(s1)+1, len(s2)+1
#     dp = [[0]*m for i in range(n)]
#     for i in range(m):
#         dp[0][i] = i
#     for j in range(n):
#         dp[j][0] = j
#     for i in range(1, n):
#         for j in range(1, m):
#             if s1[i-1] == s2[j - 1]:
#                 dp[i][j] = dp[i-1][j-1]
#             else:
#                 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
#     return dp[-1][-1]
#
# result = get_res(s1, s2)
# print(result)

import math

def iszhishu(m):
    if m == 1:
        return False
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            return False
    return True

def get_nums(n):
    ls = []
    m = 2
    if n == m:
        return ls[m]
    else:
        while n >= m:
            ll = n%m
            if ll==0:
                ls.append(m)
                n = n//m
            else:
                m = m+1
        return ls

n = int(input())
sums = 0

for i in range(2, n+1):
    if iszhishu(i):
        sums += 1
    else:
        sums += len(get_nums(i))
print(sums)


# def get_nums(n):
#     ls = []
#     m = 2
#     if n == m:
#         return ls[m]
#     else:
#         while n >= m:
#             ll = n%m
#             if ll==0:
#                 ls.append(m)
#                 n = n//m
#             else:
#                 m = m+1
#         return ls
#
# print(get_nums(6))
