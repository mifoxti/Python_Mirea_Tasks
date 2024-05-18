def main(z):
    if z < 123:
        return ((z ** 2 - 61 * z) ** 4 - 5
                * (z ** 2 + 1 + 66 * z ** 3) ** 3)
    elif 123 <= z < 197:
        return (90 * z) ** 4 + (89 * z ** 3 + z / 7
                                + z ** 2) ** 5 + 1
    elif 197 <= z < 262:
        return (1 - z ** 2) ** 7 - 1
    elif z >= 262:
        return ((z ** 3) / 95 + z ** 2 + 35 * z) ** 6


print(main((190)))
print(main((275)))
print(main((184)))
print(main((172)))
print(main((254)))