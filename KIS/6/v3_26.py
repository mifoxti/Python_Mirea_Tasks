import operator


def main(b):
    n = {2 * bm for bm in b if bm > -94 and bm <= 67}
    f = {bm ** 2 + abs(bm) for bm in b if ((bm < 42) + 2) % 2 or (bm >= -46)}
    e = {abs(fm) - fm % 3 for fm in f if
         (operator.xor((fm < 42), (fm >= -46)))}
    a = (len([nn * ee for nn in n for ee in e])
         + sum(4 * v - 9 * ee for v in n for ee in e))
    return a


# Example usage
B1 = {3, -91, -86, -76, 85, 54, 25, 91, 60, -67}
B2 = {64, 68, -54, 45, -81, 53, -43, -38, -99, -65}

print(main(B1))  # Output: -2951952
print(main(B2))  # Output: -2958272
