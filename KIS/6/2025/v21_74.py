from math import ceil, floor


def main(N):
    fi = {abs(fi) - fi ** 2 for fi in N if 11 < fi <= 51}
    omega = {vi ** 3 for vi in N if (vi >= 93 or vi <= -41)}
    keta = {ceil(f / 3) + floor(f / 6) for f in fi if (f >= 93 or f < -46)}
    delta = {om + of % 2 for om in omega for of in fi if om < of}
    aaa = {floor(beta / 3) - abs(beta) for beta in delta if beta <= 41}
    return sum(abs(ket) for ket in keta) - sum(ceil(a / 6) for a in aaa)


print(main({-32, -26, 75, -20, -49, 22, 87, 25, -36, 61}))
print(main({-64, 26, -59, 84, 53, 54, 86, 89, -38, 60}))
