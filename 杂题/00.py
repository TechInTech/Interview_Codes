"""
3 2 3
AAA
CCC
# 1
# AAA -> BBB -> CCC

*******************************

2 2 2
AA
AA
# 4
# AA -> BC -> AA
# AA -> BB -> AA
# AA -> CB -> AA
# AA -> CC -> AA
"""


integer = list(map(int, input().split()))

N, M, K = integer[0], integer[1], integer[2]

s1 = input()
s2 = input()

if s1 != s2:
    if K == N:
        result = 1
    else:
        result = 0
else:
    if K == N:
        result = K*K
    else:
        result = 0
print(result)
