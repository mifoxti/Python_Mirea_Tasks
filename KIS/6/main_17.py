def main(z):
    Trezubec = {c for c in z if (c <= 44) ^ (c >= -32)}
    NIGGER = {abs(u) + u ** 2 for u in Trezubec if (u <= 44) or (u >= 18)}
    fontan = {c ** 2 + 9 * u for c in z for u in Trezubec if c >= u}

    Sigma = sum([u % 2 - 8 * v for u in fontan for v in NIGGER])

    return len(fontan) + Sigma


print(main({36, -28, 73, 74, 16, -12, 20, -9, 90, -99}))
print(main({-62, 3, -59, -19, -67, 61, 93, -35, -2, 63}))
