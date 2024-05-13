from math import floor


def main(fontan):
    HUI = [i for i in fontan if (i < 18) ^ (i > -72)]
    Alpha = [floor(i / 2) for i in fontan if (-83 <= i < -8)]
    ooo = [(i - 2 * i) for i in Alpha if -27 <= i <= 59]
    Trezubec = [kpd * o for kpd in HUI for o in ooo if kpd < o]
    Sigma = sum([ogo * arpha for ogo in ooo for arpha in Trezubec])
    return len(ooo + Trezubec) - Sigma


print(main({1, -86, 15, 48, -47, 93, 21, -75, -99, -1}))
print(main({32, -63, 68, 74, -86, -15, 82, -71, -99, -66}))