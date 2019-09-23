# T = int(input())
#
# n = int(input())
#
# lyst = list(map(int, input().split()))
#
# flag = [1]*n
# i = 1
# while i < n:
#     if lyst[i] != lyst[i-1]:
#         flag[i], flag[i-1] = 0, 0
#         i += 2
#     else:
#         i += 1
# if sum(flag):
#     print('No')
# else:
#     print('Yes')


T = int(input())

n = int(input())

lyst = list(map(int, input().split()))

flag = [1]*n
i = 1
for i in range(n-1):
    if flag[i] == 0:
        continue
    else:
        for j in range(i+1, n):

            if flag[j] == 0:
                continue
            elif lyst[i] != lyst[j]:
                flag[i], flag[j] = 0, 0
                break
if sum(flag) != 0:
    print("NO")
else:
    print("YES")
