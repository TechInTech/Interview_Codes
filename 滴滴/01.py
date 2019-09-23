# -*- coding:utf-8 -*-

def order_by(left):
    if '/' not in left:
        while '+' in left:
            left.remove('+')
        left.sort()
        length = len(left)
        ss = ['+'] * (2*length)
        for i in range(length):
            ss[2*i] = left[i]
        return ss
    else:
        index_ = left.index('/')
        sub_left = order_by(left[0:index_-1])
        sub_right = order_by(left[index_+2::])
        ss = sub_left + left[index_-1:index_+2] + sub_right
        return ss

if __name__ == "__main__":

    """
    # 6
    # 3 + 2 + 1 + -4 * -5 + 1
    # 1 + 2 + 3 + -5 * -4 + 1

    # 11
    # -1 * -2 + 2 + 5 + -6 + -1 * -4 + -4 + 6 / 5 + -1
    # -2 * -1 + -6 + 2 + 5 + -4 * -1 + -4 + 6 / 5 + -1
    """
    n = int(input())

    operations = ['+', '-', '*', '/']

    lyst = list(map(lambda x:int(x) if x not in operations else x , input().split()))

    nums1 = lyst.count('*')

    start_list = []
    for i in range(len(lyst)):
        if lyst[i] == '*':
            start_list.append(i)

    begin = 0
    for index_ in start_list:

        if lyst[index_ - 1] > lyst[index_ + 1]:
            lyst[index_ - 1], lyst[index_ + 1] = lyst[index_ + 1], lyst[index_ - 1]

        if index_ - begin > 2:
            left = lyst[begin:index_-1]
            res = order_by(left)
            lyst = lyst[0:begin] + res + lyst[index_ - 1:index_ + 2] + lyst[index_+2::]

        if index_ + 2 < len(lyst) - 1:
            begin = index_ + 3

    print(" ".join(map(lambda x: str(x) if x not in operations else x, lyst)))
