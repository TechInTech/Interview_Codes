import math
import copy

def calc_dist(lyst1, xy, n):
    lyst = copy.copy(lyst1)
    dist = []
    counts = 0
    if xy in lyst:
        counts += lyst.count(xy)
        i = 0
        while i < counts:
            lyst.remove(xy)
            i += 1
    if n <= counts:
        return 0
    else:
        k = n - counts
        for i, j in lyst:
            dis = math.sqrt((i-xy[0])**2 + (j-xy[1])**2)
            dist.append((dis, i, j))
        dist.sort()
        nums = 0
        for i in range(k):
            nums += abs(dist[i][1] - xy[0]) + abs(dist[i][2] - xy[1])
        return nums

if __name__ == "__main__":
    n = int(input())

    lyst_x = list(map(int, input().split()))
    lyst_y = list(map(int, input().split()))

    axis = list(zip(lyst_x, lyst_y))

    nums = []
    for i in range(n):
        if i == 0:
            nums.append(0)
        else:
            counts = []
            local = (sum(lyst_x)//n, sum(lyst_x)//n)
            num = calc_dist(axis, local, i+1)
            nums.append(num)
    for i in nums:
        print(i, end=' ')
