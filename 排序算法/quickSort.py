# -*- coding:utf-8 -*-

def quicksort(lyst: list):
    quicksortHelper(lyst, 0, len(lyst) - 1)

def quicksortHelper(lyst: list, left: int, right: int):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst: list, left: int, right: int):
    middle = (left + right) // 2
    pivot = lyst[middle]

    lyst[middle], lyst[right] = lyst[right], lyst[middle]

    boundary = left
    for index_ in range(left, right):
        if lyst[index_] < pivot:
            lyst[index_], lyst[boundary] = lyst[boundary], lyst[index_]
            boundary += 1
    lyst[right], lyst[boundary] = lyst[boundary], lyst[right]
    return boundary

import random
def main(size=20, sort=quicksort):
    lyst = []
    for i in range(size):
        lyst.append(random.randint(1, size+1))
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
