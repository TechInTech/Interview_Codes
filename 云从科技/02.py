num = list(map(int, input().split()))

x, f, d, p = num[0], num[1], num[2], num[3]

days = 0
while (d > x and f > 0) or (d > (p+x) and f < 1):
    days += 1
    if f > 0:
        f -= 1
    else:
        d -= p
    d -= x

print(days)
