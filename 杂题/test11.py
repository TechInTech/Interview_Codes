# n = int(input())
# flag = list(map(int, input().split()))
#
# index_0 = []
#
# for i in range(n-1):
#     if flag[i] == 0:
#         index_0.append(i)
#
# nums = list(range(1, n+1))
#
# listnum = []
#
# for j in index_0:
#     for i in range(1, n-j-1):
#

x1, k1, x2, k2 = map(int, input().split())

def repeat(x, k):
    length = len(str(x))
    result = 0
    while k > 0:
        result += x * 10**(length*(k-1))
        k -= 1
    return result

res1 = repeat(x1, k1)
res2 = repeat(x2, k2)

print(res1, res2)

if res1 < res2:
    print("Less")
elif res1 == res2:
    print("Equal")
else:
    print("Greater")
