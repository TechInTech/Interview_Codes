# -*- coding:utf-8 -*-

if __name__ == "__main__":
    """测试样例:
    4
    abcdefg
    acdef
    acdfghijk
    cdfg
    1 2
    # 1
    2 3
    # 3
    3 4
    # 0
    """
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    while True:
        a, b = map(int, input().split())
        s1, s2 = s[a-1], s[b-1]
        nums = 0
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                break
            nums += 1
        print(nums)
