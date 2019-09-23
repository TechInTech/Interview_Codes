import sys
def get_res(x):
    if x < 10:
        return 0
    else:
        return 1
def get_res1(x):
    if x >= 10:
        return 0
    else:
        return 1

if __name__ == "__main__":
    input1 = sys.stdin.readlines()
    input2 = []
    for item in input1:
        input2.append(list(map(int, item.strip().split())))

    flag = [False]*len(input2)
    for i, item1 in enumerate(input2):
        if item1[0] >= 10 and item1[-1] >= 10:
            sub_item = item1[1:len(item1)-1]
            # res = list(filter(lambda x:x>=10, sub_item))
            res = [get_res(kk) for kk in sub_item]
            if sum(res) == 0:
                flag[i] = 'true'
        elif item1[0] < 10 and item1[-1] < 10:
            sub_item = item1[1:len(item1)-1]
            res = [get_res1(kk) for kk in sub_item]
            if sum(res) == 0:
                flag[i] ='true'
        else:
            if item1[0] < 10:
                label = True
                counts = len(item1)
                for j in range(len(item1)):
                    if label and item1[j] < 10:
                        counts -= 1
                        label = False
                    elif item1[j] >= 10:
                        counts -= 1
                        label = True
                    else:
                        break
                if counts == 0:
                    flag[i] = True
            else:
                label = True
                counts = len(item1)
                for j in range(len(item1)):
                    if label and item1[j] >= 10:
                        counts -= 1
                        label = False
                    elif item1[j] < 10:
                        counts -= 1
                        label = True
                    else:
                        break
                if counts == 0:
                    flag[i] = True
    for res in flag:
        print(res, end=' ')
