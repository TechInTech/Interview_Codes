# if __name__ == "__main__":
#     s = input()
#     ls = list(s)
#     for i in ls:
#         if i >= 'A' and i <= 'Z':
#             ls[i] = chr(ord(i) - 32)
#         elif i == ' ':
#             ls[i] = '0'
#     ls.reverse()
#     print(''.join(ls))

import sys

def get_res(item1, flag, i):
    if item1[0] >= 10 and item1[-1] >= 10:
        res = list(filter(lambda x:x>=10, item1[1:len(item1)-1]))
        if len(res) <= 0:
            flag[i] = 'true'
        return
    elif item1[0] < 10 and item1[-1] < 10:
        res = list(filter(lambda x:x<10, item1[1:len(item1)-1]))
        if len(res) <= 0:
            flag[i] = 'true'
        return
    if item1[0] < 10:
        label = True
        counts = len(item1)
        for j in range(len(item1)):
            if label and (item1[j] < 10):
                counts -= 1
                label = False
            elif item1[j] >= 10:
                counts -= 1
                label = True
            else:
                break
        if counts == 0:
            flag[i] = 'true'
    else:
        label = True
        counts = len(item1)
        for j in range(len(item1)):
            if label and (item1[j] >= 10):
                counts -= 1
                label = False
            elif item1[j] < 10:
                counts -= 1
                label = True
            else:
                break
        if counts == 0:
            flag[i] = 'true'
    return

if __name__ == "__main__":

    input1 = sys.stdin.readlines()

    input2 = []
    for item in input1:
        input2.append(list(map(int, item.strip().split())))

    if len(input2) == 0:
        print('false')
    else:
        flag = ['false']*len(input2)
        for i, item1 in enumerate(input2):
            get_res(item1, flag, i)

        for res in flag:
            print(res, end=' ')
