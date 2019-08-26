
def get_commom_small(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

n = int(input())
m = list(map(int, input().split()))

result = []
re = {}
j = 0
for i in range(n - 1):
    com = get_commom_small(m[i], m[i+1])
    print(com)
    if com > 1:
        if com in re:
            result[re[com]].extend([m[i], m[i+1]])
        else:
            re[com] = j
            result.append([m[i], m[i+1]])
            j += 1
for i in range(len(re)):

max_val = 0
for item in result:
    le = len(set(item))
    if le > max_val:
        max_val = le
# print(max_val)
print(result)
print(re)


"""
6
20 50 22 74 9 63
"""
