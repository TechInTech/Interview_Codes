import math

def isSushu(x):
    if x == 1:
        return False
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def isHuiwen(x):
    x = str(x)
    if x == x[-1::-1]:
        return True
    else:
        return False

L, R = map(int, input().split())

nums = 0

for i in range(L, R+1):
    if isSushu(i) and isHuiwen(i):
        nums += 1
print(nums)
