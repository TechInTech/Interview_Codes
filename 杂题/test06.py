# -*- coding:utf-8 -*-

import sys
size=sys.stdin.readline().strip().split()
m, n = int(size[0]), int(size[1])
maze=[[0]*n for i in range(m)]
for i in range(m):
    line=sys.stdin.readline().strip()
    maze[i]=list(line)

#钥匙的状态 就用二进制数表示 最多10 把钥匙 那就是1024
class Node:
    def __init__(self, x, y, key, step):
        self.x=x
        self.y=y
        self.key=key #key的状态用二进制表示
        self.step=step

def bfs(si,sj,m,n,maze):
    from queue import Queue
    q=Queue()
    mp=[[[0]*1025 for i in range(101)] for j in range(101)]
    nex=[[-1,0],[0,-1],[1,0],[0,1]]
    q.put(Node(si,sj,0,0))
    
    while not q.empty():
        node=q.get()
        for i in range(4):
            x=node.x+nex[i][0]
            y=node.y+nex[i][1]
            key=node.key
            if x < 0 or x >=m or y<0 or y>=n or maze[x][y]=='0':
                continue
            elif maze[x][y]=='3':
                return node.step+1
            elif 'a'<= maze[x][y] <='z':
                key=key | (1<<(ord(maze[x][y])- ord('a')))
            elif 'A'<=maze[x][y]<='Z' and (key & (1<<(ord(maze[x][y])-ord('A'))))==0:
                continue
            if mp[x][y][key]==0:
                mp[x][y][key]=1
                q.put(Node(x,y,key,node.step+1))
    return None

if __name__ == '__main__':
    for i in range(m):
        for j in range(n):
            if maze[i][j]=='2':
                print(bfs(i,j,m,n,maze))
