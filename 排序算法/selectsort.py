# -*- coding:utf-8 -*-

def selectsort(lyst: list) -> list:
    n = len(lyst)
    for i in range(n-1):
        index_ = i
        for j in range(i+1, n):
            if lyst[index_] > lyst[j]:
                index_ = j
        if index_ != i:
            lyst[i], lyst[index_] = lyst[index_], lyst[i]
    return lyst


if __name__ == "__main__":
    lyst = [49, 38, 65, 97, 76, 13, 27, 49]
    print(lyst)
    print(selectsort(lyst))
