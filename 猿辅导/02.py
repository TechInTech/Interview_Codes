n, m = map(int, input().split())

lyst = list(map(int, input().split()))

flag = [0]*n
for i in range(n):
    if lyst.count(lyst[i]) > m:
        flag[i] = 1

result = []
for i in range(n):
    if flag[i] == 0:
        result.append(lyst[i])
print(' '.join(map(str, result)))
