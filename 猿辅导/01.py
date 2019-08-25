"""
3
3 1 1 1
3 2 2 3
4 0 2 3 99
"""

C = int(input())

i = 0
test = []
while i < C:
    lyst = list(map(int, input().split()))
    i += 1

    m = lyst[0]
    sub = lyst[1::]
    sub.sort()
    nums = 0
    while len(sub) >= 3:
        while sub[0] == 0:
            sub.pop(0)
        if len(sub) >= 3:
            nums += sub[0]
            sub[1] = sub[1] - sub[0]
            sub[2] = sub[2] - sub[0]
            sub = sub[1::]
            # sub.sort()
        else:
            nums += 0
    print(nums)
