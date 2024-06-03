from math import ceil, log10, log2


def main(z):
    if z < 70:
        return z ** 2 - 46 * z ** 12 - 60 * ceil(z)
    elif 70 <= z < 157:
        return log2(z ** 3 - z ** 2 / 77 - z) ** 5
    elif 157 <= z < 237:
        return (16 * log10(34 * z) ** 6 - z ** 3
                - 71 * (85 * z + 75 * z ** 3 + z ** 2) ** 2)
    elif z >= 237:
        a = (abs(53 * z ** 2 - z - 1)) ** 3 / 94
        b = 89 * (z + 98 * z ** 2) ** 7 + z ** 4 / 44
        return a + b


print(main((90)))
print(main((147)))
print(main((161)))
print(main((99)))
print(main((169)))
