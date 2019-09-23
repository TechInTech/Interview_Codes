def get_fib(fib, n):
    if n not in list(range(len(fib))):
        for i in range(len(fib), n+1):
            fib.append(fib[i-1] + fib[i-2])
    return fib[n], fib

if __name__ == '__main__':
    n = int(input())

    fib = [0, 1]
    max_val = float('inf')
    size_ = 0
    for i in range(n+1):
        resu, fib = get_fib(fib, i)
        #print(resu)
        diff = abs(n - resu)
        if diff < max_val:
            max_val = diff
        if diff > max_val:
            break
    print(max_val)
