# # lyst = list(map(int, input().split(',')))
# #
# # nums = [1]*len(lyst)
# #
# # for i in range(len(lyst)-1):
# #     if i == len(lyst)-1:
# #         break
# #     for j in range(i+1, len(lyst)):
# #         if lyst[i] > lyst[j]:
# #             nums[i] = 0
# #             break
# #
# # print(sum(nums))
# n = int(input())
#
# highs = list(map(int, input().split()))
#
# highs.sort()
#
# left = 1
# right = n - 1
#
# ll = [highs[0]]
#
# while left < right:
#     r0 = abs(ll[0] - highs[right])
#     r1 = abs(ll[-1] - highs[right])
#     l0 = abs(ll[0] - highs[left])
#     l1 = abs(ll[-1] - highs[left])
#
#     rl = [r0, r1, l0, l1]
#
#     m = max(rl)
#     if rl.index(m) == 0:
#         ll.insert(0, highs[right])
#         right -= 1
#     if rl.index(m) == 1:
#         ll.append(highs[right])
#         right -= 1
#     if rl.index(m) == 2:
#         ll.insert(0, highs[left])
#         left += 1
#     if rl.index(m) == 3:
#         ll.append(highs[left])
#         left += 1
#
# nums = 0
# for i in range(n-1):
#     nums += abs(ll[i] - ll[i+1])
# print(nums)

# lyst = list(map(int, input().split()))
#
# for i in range(1, len(lyst)):
# 	lyst[i] = lyst[i] + max(nums[i-1], 0)
#
# print(max(lyst))



# min_price = lyst[0]
# max_p = 0
# res = []


lyst = list(map(int, input().split()))

l1 = [0]*len(lyst)
l2 = [0]*len(lyst)

s1 = lyst[0]

for i in range(1, len(lyst)):
    s1 = max(s1, l1[i]-lyst[i])
    l1[i] = max(l1[i-1], s1+lyst[i])
s2 = lyst[0]
for i in range(1, len(lyst)):
    s2 = max(s2, l1[i] - lyst[i])
    l2[i] = max(l2[i-1], s2+lyst[i])

print(l2[-1])
