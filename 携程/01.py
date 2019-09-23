
s = input()

nums = []
i = 0
while i < len(s):
    ss = s[i]
    if ss in s[i+1:]:
        for j in range(len(s) - 1, i, -1):
            if s[j] == ss:
                break
        max_index_ = j
        for l1 in range(i+1, j):
            if s[l1] in s[j+1:]:
                index_ = s[j+1:].index(s[l1])
                v = j + 1 + index_
                if max_index_ < v:
                    max_index_ = v
        nums.append(max_index_ - i + 1)
        i = max_index_ + 1
    else:
        nums.append(1)
        i += 1
print(','.join(map(str, nums)))
