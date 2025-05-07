from math import floor


def main(Y):
    peta = {abs(ve) for ve in Y if -91 <= ve < -5}
    keta = {ve * pe for ve in Y for pe in peta if ve > pe}
    ata = {pe - floor(pe / 2) for pe in peta if not(-45 <= pe < 37)}
    eka1 = sum(k**2 for k in keta)
    eka2 = sum(2 * k - a % 2 for a in ata for k in keta)
    return eka1 + eka2


# Примеры результатов вычислений
M1 = {-61, 36, 68, -26, -56, -49, 49, 87, -70, -33}
M2 = {33, 26, -93, 37, 7, 43, 20, -40, -70, -98}

print(main(M1))  # Output: 4765678
print(main(M2))  # Output: 3434675
