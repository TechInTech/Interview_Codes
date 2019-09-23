# -*- coding：utf-8-*-
import  sys
if __name__ == '__main__':
    # 候选人数
    a,b=map(int,input().strip().split())
    c=list(map(int,sys.stdin.readline().strip().split()))
    d=list(map(int,input().strip().split()))
    c=sorted(c)
    d=sorted(d)
    e=[]
    for i in range(a):
       for j in range(a-1,-1,-1):
          if c[i]+d[j]<b and c[i]!=-1 and d[j]!=-1:
             e.append(c[i]+d[j])
             d[j] = -1
             c[i] = -1
    c=sorted(c)
    d=sorted(d)
    print(c, d, e)
    # for i in range(a):
    #    if c[i]!=-1:
    #       e.append(c[i]+d[i])
    # for i in range(a):
    #    e[i]=e[i]%b
    # e=sorted(e)
    # for i in range(a-1,-1,-1):
    #    print(e[i],end=' ')
