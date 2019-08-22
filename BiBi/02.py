# -*- coding:utf-8 -*-

if __name__ == "__main__":

# """
# 3 3
# 40 24 135
# 200 239 238
# 90 34 94
# 2
# 0.0 0.6
# 0.1 0.3
# """

    h, w = map(int, input().split())

    photo = []

    for i in range(h):
        photo.append(list(map(int, input().split())))

    m = int(input())

    kernal = []
    for i in range(m):
        kernal.append(list(map(float, input().split())))

    result = []
    for i in range(0, h - m + 1):
        sub_res = []
        line = photo[i:i+m]
        for j in range(0, w - m + 1):
            ss = 0
            for k1 in range(m):
                for k2 in range(m):
                    ss += line[k1][j+k2]*kernal[k1][k2]
            sub_res.append(int(ss))
        result.append(sub_res)

    for i in range(len(result)):
        print(" ".join(map(str, result[i])))
