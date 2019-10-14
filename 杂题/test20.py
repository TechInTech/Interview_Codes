# 携程3
def get_squareroot(n, littlenum):
    n1 = n
    n2 = 1.0
    while (n1 - n2) > littlenum:
        n1 = (n1 + n2) / 2
        n2 = n / n1
    return n1

if __name__ == "__main__":
    # 给定的数
    n = int(input())

    # 设定精度
    smallnum  = 0.0000001

    res = get_squareroot(n, smallnum)
    print("%.4f"%res)
