# N, M = map(int, input().split())
#
# lyst = []
# i = 0
# while i < M:
#     lyst.append(int(input()))
#     i += 1
#
# node = list(range(1, N + 1))

ll = list(map(int, input().split()))
n, p, q = ll[0], ll[1], ll[2]

def get(ll, m):
    res = 1
    for i in range(ll, m+1):
        fenmu = 1
        j = 1
        while j <= i:
            fenmu *= j
            j += 1

        fenzi = 1
        while m >= i:
            fenzi *= m
            m -= 1
        res += fenzi//fenmu
    # print(res)
    return res

def sub_get(i, m):
    if i == m:
        return 1
    res = 0
    fenmu = 1
    j = 1
    while j <= i:
        fenmu *= j
        j += 1

    fenzi = 1
    while m >= i:
        fenzi *= m
        m -= 1
    res += fenzi//fenmu
    return res

he = 0
for i in range(p, n+1):
    he += sub_get(i, n) * i

hh = get(p, n)

res = (he//hh)mod()1000000007
print(res)
