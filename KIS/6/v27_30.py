from math import floor


def main(o):
    b = {5 * om - om for om in o if 32 <= om < 84}
    i = {ori ** 2 for ori in o if ori > -61}
    liti = {li ** 3 for li in i if -66 <= li < 86}
    fontan = {floor(beta / 4) for beta in b if (beta > -55 or beta <= 38)}
    return len([(lll * fi) for fi in fontan for lll in liti]) + sum(fontan)

print(main({-28, 69, -22, -19, -49, 19, -76, -10, -9, -37}))
print(main({-63, -27, -89, -56, -52, -76, 54, -74, -5, -99}))
