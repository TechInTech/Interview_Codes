n, m = map(int, input().split())

p = 0

def get_prob(p, n, m):
    if m < 3:
        p += n/(m+n)
        return p

    p = m/(m+n)


    p *= n/(m+n)
    m -= 1

    p = get_prob(p, n, m)

    m -=2
    n -= 1
    p += n/(m+n)
    m += 2
    n += 1

    p = get_prob(p, n, m)

    return p

pro = get_prob(p, n, m)

print("%.5f"%pro)
