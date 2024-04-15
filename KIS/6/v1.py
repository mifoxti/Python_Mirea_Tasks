from math import ceil, floor


def main(OOO):
    box = {ceil(o / 4) for o in OOO if (o >= -60 or o < -7)}
    M = {o * e for o in OOO for e in box if o < e}
    OMEJKA = {floor(e / 8) + e ** 3 for e in box if -38 <= e < 72}

    SIGMA = sum([q * w for q in M for w in OMEJKA])

    return len(M) - SIGMA


print(main({97, 35, -26, -85, 14, 19, -44, -12, -43, 60}))
print(main({-96, -64, 68, 69, 38, -89, -20, 51, 53, -98}))
