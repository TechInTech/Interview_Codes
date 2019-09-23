# import math
#
# n = int(input())
# scores = []
# i = 0
# while i < n:
#     scores.append(int(input()))
#     i += 1
#
# scores.sort(reverse=True)
#
# k = math.ceil(0.001*n)
#
# for i in range(k):
# 	print(scores[i])

import heapq
import math

class BigHeap:
    def __init__(self):
        self.arr = list()
    def heap_insert(self, val):
        heapq.heappush(self.arr, -val)
    def heapify(self):
        heapq.heapify(self.arr)
    def heap_pop(self):
        return -heapq.heappop(self.arr)
    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]

n = int(input())
scores = BigHeap()
i = 0
while i < n:
    scores.heap_insert(int(input()))
    i += 1

k = math.ceil(0.001*n)

for i in range(k):
    print(scores.heap_pop())

# k_large = heapq.nlargest(k, scores)
#
# for i in k_large:
#     print(i)
