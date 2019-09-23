s1 = input()
s2 = input()

nums = []
flag = True

for i in s2:
    if i in s1:
        index_ = s1.index(i)
        nums.append(index_)
        s1 = s1.replace(i, '#', 1)
    else:
        flag = False
        break

if flag:
    flag1 = True
    for j in range(len(nums)-1):
        if nums[j] < nums[j+1]:
            pass
        else:
            flag1 = False
            break
    if flag1:
        print(1)
    else:
        print(0)
else:
    print(0)
