#
# n, m = map(int, input().split())
#
# lyst = list(map(int, input().split()))
#
# flag = [0]*n
# for i in range(n):
#     if lyst.count(lyst[i]) > m:
#         flag[i] = 1
#
# result = []
# for i in range(n):
#     if flag[i] == 0:
#         result.append(lyst[i])
# print(' '.join(map(str, result)))
"""
# 3
# 3 1 1 1
# 3 2 2 3
# 4 0 2 3 99
"""



# C = int(input())
#
# i = 0
# test = []
# while i < C:
#     test.append(list(map(int, input().split())))
#     i += 1
#
# for lyst in test:
#     m = lyst[0]
#     sub = lyst[1::]
#     sub.sort()
#     while sub[0] == 0:
#         sub.pop(0)
#     if len(sub) >= 3:
#         print(sub[0])
#     else:
#         print(0)

# C = int(input())
#
# i = 0
# test = []
# while i < C:
#     test.append(list(map(int, input().split())))
#     # lyst = list(map(int, input().split()))
#     i += 1
#
# for lyst in test:
#     m = lyst[0]
#     if m >= 3:
#         sub = lyst[1::]
#         sub.sort()
#         while sub[0] == 0:
#             sub.pop(0)
#         if len(sub) >= 3:
#             print(sub[0])
#         else:
#             print(0)
#     else:
#         print(0)


C = int(input())

i = 0
test = []
while i < C:
    test.append(list(map(int, input().split())))
    i += 1

for lyst in test:
    m = lyst[0]
    if m >= 3:
        sub = lyst[1::]
        sub.sort()
        if 0 in sub:
            nums = sub.count(0)
            while nums > 0:
                sub.remove(0)
                nums -= 1
        #while sub[0] == 0:
        #    sub.pop(0)
        if len(sub) >= 3:
            sub.sort()
            print(sub[0])
        else:
            print(0)
    else:
        print(0)
