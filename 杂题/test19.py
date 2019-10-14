# -*- coding:utf-8 -*-
## 携程1

def bianji_distance(str1,str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    len1 = len(str1) + 1
    len2 = len(str2) + 1

    dp = [[0]*len2 for x in range(len1)]

    for i in range(len1):
        dp[i][0] = i
    for j in range(len2):
        dp[0][j] = j

    for i in range(1,len1):
        for j in range(1,len2):
            del_num = dp[i-1][j] + 1
            ins_num = dp[i][j-1] + 1
            rep_num = dp[i-1][j-1]
            if str1[i-1] != str2[j-1]:
                rep_num += 1
            dp[i][j] = min(ins_num,del_num,rep_num)

    return dp[len1-1][len2-1]

if __name__ == "__main__":
    A, B = input().split("<ctrip>")
    print(bianji_distance(A,B))
