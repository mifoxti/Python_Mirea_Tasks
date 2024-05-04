from math import ceil, floor


def main(fontan):
    hhh = {v + v for v in fontan if v not in range(-39, 3)}
    bbb = {2 * n - n % 2 for n in hhh if (n > -11) ^ (n <= 95)}
    aaa = {v for v in fontan if v <= -7 or v > -81}
    Sigma = sum([a ** 3 + b for a in aaa for b in bbb])
    return len(aaa) + Sigma


print(main({-63, -95, -60, -51, 78, -78, 50, -39, -35}))
print(main({-62, 69, -27, 73, 45, 14, -79, -78, 19, 86}))
