def sift(li, low, high):
    i = low
    j = 2 * i + 1
    temp = li[low]
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j += 1
        if li[j] < temp:
            li[i] = li[j]
            i = j
            j = 2*i + 1
        else:
            li[i] = temp
            break
    else:
        li[i] = temp

def topk(li, k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k - 1)
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap

import random

if __name__ == "__main__":

    li = list(range(100))
    random.shuffle(li)
    print(li)
    print(topk(li, 5))
