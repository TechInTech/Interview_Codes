# -*- coding:utf-8 -*-
import sys

if __name__ == '__main__':
    str_input = sys.stdin.readline().strip().split(' ')

    sub_str = []
    for i in str_input:
        if len(i) > 1:
            sub_str.append(i[0] + i[-1])
        else:
            sub_str.append(i[0])
    # print(sub_str)
    str_dict = {}
    flag = True
    while flag:
        for item in sub_str:
            if len(item) == 1:
                if item in str_dict.values():
                    key = list(str_dict.keys())[list(str_dict.values()).index(item)]
                    str_dict[key] = item
                else:
                    str_dict[item] = item
            else:
                if item[0] in str_dict.values():
                    key = list(str_dict.keys())[list(str_dict.values()).index(item[0])]
                    str_dict[key] = item[-1]
                else:
                    str_dict[item[0]] = item[-1]

        list_dict = []
        for k1, it1 in str_dict.items():
            list_dict.extend([k1, it1])

        if len(str_dict) == 1 or len(set(list_dict)) >= 3:
            flag = False
        else:
            sub_str = []
            for k, it in str_dict.items():
                sub_str.append(k + it)
            str_dict = {}

    if len(str_dict) > 1 or (len(str_dict) == 1 and list(str_dict.keys())[0] != list(str_dict.values())[0]):
        print(False)
    else:
        print(True)
