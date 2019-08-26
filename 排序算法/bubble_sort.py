# -*- coding:utf-8 -*-

def bubble_sort(array: list) -> list:
    """冒泡排序"""
    n = len(array)
    j = 0
    while j < n:
        min_val = array[j]
        index = j
        for i in range(j, n):
            if array[i] < min_val:
                min_val = array[i]
                index = i
        del array[index]
        array.insert(j, min_val)
        j += 1
    return array

def bubbleSort(array: list) -> list:
    n = len(array)
    while n > 0:
        i = 1
        while i < n:
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            i += 1
        n -= 1
    return array

if __name__ == "__main__":
    array = [49, 38, 65, 97, 76, 13, 27, 49]

    print(bubble_sort(array))
    # print(bubbleSort(array))
