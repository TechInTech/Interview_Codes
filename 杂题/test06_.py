# -*- coding:utf-8 -*-
from queue import Queue

class Node:
    def __init__(self, x, y, key, step):
        self.x = x
        self.y = y
        self.key = key
        self.step = step

def bfs(si,sj, m, n, maps):
    q = Queue()
    maps_init = [[[0]*1025 for i in range(101)] for j in range(101)]
    next_dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    q.put(Node(si, sj, 0, 0))

    while not q.empty():
        node = q.get()
        for i in range(4):
            x = node.x + next_dir[i][0]
            y = node.y + next_dir[i][1]
            key = node.key
            if x < 0 or x >= m or y < 0 or y >= n or maps[x][y] == "0":
                continue
            elif maps[x][y] == "3":
                return node.step + 1
            elif "a" <= maps[x][y] <= "z":
                key = key | (1 << (ord(maps[x][y]) - ord("a")))
            elif "A" <= maps[x][y] <= "Z" and (key & (1 << (ord(maps[x][y]) - ord("A")))) == 0:
                continue
            if maps_init[x][y][key] == 0:
                maps_init[x][y][key] = 1
                q.put(Node(x, y, key, node.step+1))
    return None

if __name__ == "__main__":
    M, N = map(int, input().split())

    maps = []
    for i in range(M):
        line = list(input())
        maps.append(line)
        if "2" in line:
            enter = [i, line.index('2')]
    print(bfs(enter[0], enter[1], M, N, maps))
