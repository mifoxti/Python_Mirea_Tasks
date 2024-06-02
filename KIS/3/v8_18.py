def main(n, b, a):
    res = 0
    for j in range(1, a + 1):
        ms = 0
        for i in range(1, b + 1):
            ms2 = 0
            for c in range(1, n + 1):
                ms2 += (90 * c ** 2 + (j ** 2 + i ** 3 / 34) ** 4)
            ms += ms2
        res += ms
    return res
