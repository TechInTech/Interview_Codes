"""
5
33956 27538
79731 91415
25288 33956
33956 84925
79731 25288

# 79731
"""

n = int(input())

i = 0
lyst = []
while i < n:
    lyst.append(list(map(int, input().split())))
    i += 1

tree = {}
seed = []
for i in range(n-1):
    if i in seed:
        continue
    line = lyst[i]
    for j in range(i+1, n):
        if j in seed:
            continue
        if lyst[j][1] == line[0]:
            seed.append(j)
            line.insert(0, lyst[j][0])

    if line[0] in tree.keys():
        tree[line[0]].extend(line[1::])
    else:
        tree[line[0]] = line[1::]

max_val = [0, 0]
for key in tree.keys():
    if len(tree[key]) > max_val[0]:
        max_val[0] = len(tree[key])
        max_val[1] = key
    elif len(tree[key]) == max_val[0]:
        if max_val[1] < key:
            max_val[1] = key

print(max_val[1])
