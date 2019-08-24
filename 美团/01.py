# -*- coding:utf-8 -*-

def longestCommonPrefix(strs) -> str:
    """求字符串数组的最长前缀字符串
    """
    n = len(strs)
    s = ""
    if n == 0:
        return s
    else:
        length = [len(strs[i]) for i in range(n)]
        short = min(length)
        short_index = length.index(short)
        for j in range(short):
            for x in range(n):
                if x == short_index:
                    continue
                elif strs[x][j] != strs[short_index][j]:
                    return s
            s += strs[short_index][j]
        return s

def sort_str(lyst: list, m: int):
    # 保证lyst长度大于等于2

    lyst_group = []

    # 判断是否有前缀字符串
    s = longestCommonPrefix(lyst)
    if s != '': # 有前缀字符串
        sub_s = s
        counts = lyst.count(s)
        m = len(s)
        while counts > 0:
            lyst.remove(s)
            counts -= 1
            lyst_group.append([s])

    n = len(lyst)
    if n < 2:
        lyst_group.append(lyst)
    else:
        j = 0
        # 选择排序
        while n > 0:
            i = j
            index_ = j
            while i < len(lyst):
                if lyst[i][m] > lyst[index_][m]:
                    index_ = i
                i += 1
            if index_ != j:
                lyst[j], lyst[index_] = lyst[index_], lyst[j]
            j += 1
            n -= 1
        # 字符串数组按相同的字符串分组
        # 以下需要保证len(lyst) >= 2
        start, end = 0, 1
        lyst_group.append([lyst[start]])
        while True:
            if lyst[end-1][m] == lyst[end][m]:
                lyst_group[-1].append(lyst[end])
            else:
                lyst_group.append([lyst[end]])
            end += 1
            if end == len(lyst):
                break
    return lyst_group

def get_result(lyst: list, m: int):
    """采用递归的方法，对字符串数组进行排序"""
    if len(lyst) == 1:
        return lyst

    # 将字符串数字按具有相同的前缀的进行分组，得到分组后的字符串数组列表
    lyst_group = sort_str(lyst, m)
    m += 1

    result = []
    # 遍历每一个组成分(列表)
    for sub_lyst in lyst_group:
        # 递归进行排序
        result.extend(get_result(sub_lyst, m))
    return result

if __name__ == "__main__":
    # s = list(input().split(','))
    s = 'waimai,dache,lvyou,liren,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian'
    print(s)
    s = s.split(',')

    nums = 0
    # step 1: 判断字符串中是否有空字符，如有空字符，将其提出来，放置排序后的字符串首位
    if '' in s:
        nums = s.count('')
        while '' in s:
            s.remove('')
    s1 = ['']*nums

    # step 2: 余下字符串按字符逐个比较，按z-a进行排序，从第0个字符开始
    result = get_result(s, 0)
    s1.extend(result)
    print(','.join(s1))
