# -*- coding:utf-8 -*-

"""解题思路：首先将规定的积木按边长的由小到大排序，由小到大一次遍历排序好的积木，
边长小的积木在上头，边长大的在下面；按边长大小堆放积木时，保证上面积木的总重量小
于等于其自身重量的7倍。解决这类问题的方法采用递归的思想，
"""

import sys


if __name__ == '__main__':

    print('输入积木的数量:')
    n = int(sys.stdin.readline().strip())

    print('输入积木的长宽度列表:')
    length = list(map(lambda x: int(x), sys.stdin.readline().strip().split(' ')))

    print('输入积木的重量:')
    weight = list(map(lambda x: int(x), sys.stdin.readline().strip().split(' ')))

    print('length: ', length)
    print('weight: ', weight)

    """
    # 测试
    n = 4
    length = [1, 2, 3, 4, 5, 6]
    weight = [1, 2, 12, 2, 3, 1]
    """

    if n == 1:
        print(n)
    else:

        # 递归子函数
        def find_high(length_w, n, high_, nums, sum_weight):
            """
            Parameters：
            ----------
            length_w (list(tuple)): 包含元组的列表(元组为积木对应的边长和重量)，
                                    且列表按元组首元素由小到大排序；
            n (int): 列表当前元素的索引；
            high_ (list): 积木每高一层就将层数存入该列表中
            nums (n): 增加的层数
            sum_weight (int): 上面积木的总重量
            """
            for j in range(n+1, len(length_w)):
                # 如果积木总重量大于当前积木所承受的最大重量，跳过当前积木
                if sum_weight > 7*length_w[j][1]:
                    continue
                # 否则，增加层数，累计积木总重量
                else:
                    sum_weight += length_w[j][1]
                    nums += 1
                    high_.append(nums)
                    # 当遍历到边最大的积木时，停止遍历，并将增加的层数、积木重量减去
                    if j == len(length_w) - 1:
                        nums -= 1
                        sum_weight -= length_w[j][1]
                        break
                    high_, nums, sum_weight = find_high(length_w, j, high_, nums, sum_weight)
                    # 减去该层的积木层数、重量，相当于跳过该层，计算下面边长的积木
                    nums -= 1
                    sum_weight -= length_w[j][1]

            return high_, nums, sum_weight

        # 将长度重量转化为元组列表:（长度,重量)
        length_w = zip(length, weight)
        # 将列表按元组第一个元素排序
        length_w = sorted(length_w, key=lambda x: x[0])

        high_ = []
        # 由于没有在此处遍历列表最后一个元组，其相当没有考虑只有最后一个积木成立的情况
        for i in range(len(length_w)-1):
            nums = 1
            sum_weight = length_w[i][1]
            high_, nums, sum_weight = find_high(length_w, i, high_, nums, sum_weight)

        # 在此加上没有考虑的最后一种情况
        high_.append(1)
        print(max(high_))
