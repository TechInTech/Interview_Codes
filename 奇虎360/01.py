# -*- coding:utf-8 -*-
"""
# 将长为N*M厘米的矩形区域划分为N行M列(每行每列的宽度均为1厘米)，
# 在第i行第j列的位置上叠放A_ij个边长为1厘米的正方体(1<=A_ij<=100),
# 所有的正方体就组成了一个立体图形，每个正方体6个面的一部分都会被其它
# 正方体遮挡，未被遮挡的部分的总面积即为该立方体图形的表面积，该立体图形的表面积为多少；
# leetcode 892原题
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 解题思路 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## 当单个立方体的个数A_ij=0时，对应的表面积为square_{ij}=0
## 当单个立方体的个数A_ij >= 1时，对应的表面积为square_{ij} = 6 + (A_ij - 1) * 4 -
## (min(A_ij, A_{i-1}j) + min(A_ij, A_{i+1}j) + min(A_ij, A_i{j-1}) +
## min(A_ij, A_i{j+1}))，其中如果i, j满足
## i - 1 >= 0; i + 1 <= n-1; j - 1 >= 0; j + 1 <= m - 1
## 立方体图形的表面积为所有立方体square_{ij}(i=[0,n-1], j=[0, m-1])的表面积之和
"""

def count_interface(matrix, i, j, n, m):
    counts = 0
    current = matrix[i][j]
    if i - 1 >= 0:
        counts += min(current, matrix[i - 1][j])
    if i + 1 <= n - 1:
        counts += min(current, matrix[i + 1][j])
    if j - 1 >= 0:
        counts += min(current, matrix[i][j - 1])
    if j + 1 <= m - 1:
        counts += min(current, matrix[i][j + 1])
    return counts

if __name__ == '__main__':
    # 候选人数
    n, m = map(int,input().split())
    ls1 = []

    for _ in range(n):
        ls1.append(list(map(int, input().split())))

    result = 0
    for i in range(n):
        for j in range(m):
            cubes_ = ls1[i][j]
            if cubes_ == 0:
                square = 0
            else:
                square = 6 + (cubes_ - 1) * 4
                nums = count_interface(ls1, i, j, n, m)
                square -= nums
            result += square
    print(result)
