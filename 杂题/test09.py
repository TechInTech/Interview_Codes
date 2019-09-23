"""
4
1 2 4 9
1 1 1 1

# 0 1 3 10
"""

import math

n = int(input())

lyst_x = list(map(int, input().split()))
lyst_y = list(map(int, input().split()))

steps = [math.inf]*n

for x in lyst_x:
    for y in lyst_y:
        num = 0
        dist = sorted([abs(x - lyst_x[i]) + abs(y - lyst_y[i]) for i in range(n)])
        for i in range(n):
            num += dist[i]
            if num < steps[i]:
                steps[i] = num

print(" ".join(map(str, steps)))
