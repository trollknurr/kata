def decompose(n):
    n2 = n ** 2
    data = []
    r = n - 1
    while r > 0:
        r2 = r ** 2
        if r2 <= n2:
            n2 -= r2
            data.insert(0, r)
            print n2
        r -= 1
    return data


print decompose(50)
