# -*- coding:utf-8 -*-

if __name__ == '__main__':
    # a, b = 5, 17
    #
    # flag = True
    # while flag:
    #     sum1 = a^b
    #     carry = (a&b)<<1
    #
    #     a = sum1
    #     b = carry
    #     if b == 0:
    #         flag = False
    # print(a)


    s = ')12-345'
    def check(s1):
            if s1 >= '1' and s1 <= '9':
                return s1
            else:
                return ''
    s2 = ''.join(map(lambda x:check(x), s))
    print(int(s2))
