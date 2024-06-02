from math import ceil


def main(phi):
    orix = {2 * fi for fi in phi if fi < 33}
    omega = {fi * epsi for fi in phi for epsi in orix if fi <= epsi}
    ogo = {ceil(epsi / 4) for epsi in orix if epsi <= -12}
    return len(omega) + sum([wi * ooo for wi in omega for ooo in ogo])


print(main({-28, 72, -20, 45, -13, -76, -71, 60, 61, 62}))
print(main({64, 67, 4, -25, -18, -48, 49, -72, -39, -98}))
