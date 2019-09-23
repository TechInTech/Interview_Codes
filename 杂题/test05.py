# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # n = int(input())
    line = open('data.txt')
    integers = list(map(int, line.readline().strip().split()))
    # print(integers)
    # integers = list(map(int, input().split()))
    line.close()

    neg = list(filter(lambda x:x<0, integers))
    pos = list(filter(lambda x:x>=0, integers))
    # print("neg: ", neg)
    # print("pos: ", pos)
    if len(neg) <= 1:
        pos.sort()
        max_val = pos[-1] * pos[-2] * pos[-3]
    else:
        pos.sort()
        neg.sort()
        print("neg: ", neg)
        print("pos: ", pos)
        mul_neg = neg[0] * neg[1]
        mul_pos = pos[-1] * pos[-2]
        if mul_neg > mul_pos:
            max_val = mul_neg * pos[-1]
        else:
            max_val = mul_pos * pos[-3]
    print(max_val)
