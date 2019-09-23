# #
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next=None
# #
# # class Solution:
# #     def reverseListnode(self, head):
# #         if not head or not head.next:
# #             return head
# #
# #         cur = head
# #         pre = None
# #         while cur:
# #             temp = cur.next
# #             cur.next = pre
# #             pre = cur
# #             cur = temp
# #         return pre
#
# # if __name__ == "__main__":
# #     T = int(input())
# #     while T > 0:
# #         T -= 1
# #         lyst = list(map(int, input().split()))
# #         lyst.sort()
# #         while lyst[-1] - lyst[0] >= 1:
# #             lyst[0] += 1
# #             lyst[-1] -= 1
# #             lyst.sort()
# #         print(max(lyst))
# # if __name__ == "__main__":
# #     n = int(input())
# #     lyst = list(map(int, input().split()))
# #
# #     pairs = 0
# #     for i in range(len(lyst)-1):
# #         for j in range(i, len(lyst)):
# #             if lyst[i] > lyst[j]:
# #                 pairs += abs(i-j)
# #     print(pairs)
# # import copy
# #
# # if __name__ == "__main__":
# #     n = int(input())
# #     lyst = list(map(int, input().split()))
# #
# #     pairs = 0
# #     for i in range(len(lyst)-1):
# #         if min(lyst[i+1:]) > lyst[i]:
# #             continue
# #         else:
# #             lyst_copy = copy.deepcopy(lyst)
# #             while min(lyst_copy[i+1:]) < lyst[i]:
# #                     index_ = lyst_copy.index(min(lyst_copy[i+1:]))
# #                     pairs += abs(i-index_)
# #                     lyst_copy[index_] = lyst[i]
# #     print(pairs)
# # if __name__ == "__main__":
# #     T = int(input())
# #     n, m = map(int, input().split())
# #     lyst = list(map(int, input().split()))
# #     res1 = sum(lyst) + m
# #     res2 = ((n-1)*n)//2
# #     if res1 >= res2:
# #         print("YES")
# #     else:
# #         print("NO")
#
# # def des(x, y):
# #     if y%2 == 0:
# #         return False
# #     return True
# #
# # if __name__ == "__main__":
# #     n = int(input())
# #     while n > 0:
# #         n -= 1
# #         m = int(input())
# #         res = 0
# #         counts = 0
# #         for i in range(1, m):
# #             for j in range(i+1, m+1):
# #                 if des(i, j):
# #                     counts += 1
# #                     res += i*j
# #         if counts == 0:
# #             print(2)
# #         elif res%counts == 0:
# #             print("%d"%res//counts)
# #         else:
# #             print("%d/%d"%(res, counts))
#
#
# if __name__ == "__main__":
#     n, k, m = list(map(int,input().split()))
#     s1 = input()
#     s2 = input()
#
#     counts = 0
#     for i in range(n):
#         if s1[i] == s2[i]:
#             counts += 1
#     diff = n - counts
#     if  diff//m == k:
#         f = 1
#         for i in range(diff, diff-m-1, -1):
#             f *= i
#         fm = 1
#         for i in range(1, m+1):
#             fm *= i
#
#     res = f//fm
#     res = res%1000000009
#     print(res)

# if __name__ == '__main__':
#     strs = ['`','!','@','#','$','%','^','&','*','(',')','{','}',"\\",'<','>','?']
#     # str_dict = {}
#     # for i in range(27):
#     #     if i > 9:
#     #         str_dict[i] = strs[i-10]
#     #     else:
#     #         str_dict[i] = str(i)
#
#     n = int(input())
#     s = ""
#     while n >= 27:
#         fir, sco = divmod(n, 27)
#         if sco < 10:
#             sco = str(sco)
#         else:
#             sco = strs[sco-10]
#         s = sco + s
#         n = fir
#     if n > 10:
#         n = strs[n-10]
#     else:
#         n = str(n)
#     s = n+s
#     print(s)
# import math
# if __name__ == "__main__":
#     lyst = list(map(int, input().split(',')))
#     rate = lyst[0]
#     nums = lyst[1::]
#
#     n = len(nums)
#
#     all_ = math.ceil(n*0.01*rate)
#     nums.sort(reverse=True)
#     for i in range(all_):
#         print(nums[i], end=' ')

if __name__ == "__main__":
    email = input()
    index_ = email.index('@')
    last = email[index_:]
    mask = "MASK"
    j = 0
    s = ''
    for i in range(index_):
        if j == 4:
            j = 0
        s = s + email[i]
        if i == index_-1:
            break
        s = s+mask[j]
        j += 1
    print(s+last)
