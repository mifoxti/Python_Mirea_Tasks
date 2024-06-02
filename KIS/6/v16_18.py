from math import ceil
from operator import xor


def main(omega):
    nigger = {ceil(w / 2) - w % 3 for w in omega if -72 < w < 31}
    hike = {w for w in omega if (xor(w >= -27, w < 61))}
    mega_haha_pachka_chipsov_hah_s_krabom_leys = nigger | hike
    ogo = {n - n % 3 for n in hike if n > -48}
    ten_black_kids = {u * e
                      for u in mega_haha_pachka_chipsov_hah_s_krabom_leys
                      for e in ogo if u <= e}
    sex_pressure = 1
    for e in ogo:
        for v in ten_black_kids:
            sex_pressure *= (e % 3 + v % 3)
    return sum([8 * e for e in ogo]) - sex_pressure


print(main({-93, -61, 40, 8, -85, 79, -71, 27, 30, 31})) # = 624
print(main({65, -88, 9, 44, -78, -77, 20, 23, 90, 29})) # = 1224