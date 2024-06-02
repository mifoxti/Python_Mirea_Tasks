from math import floor


def main(treugolnik):
    pika_tochenaya = {floor(b / 4) + b
                      for b in treugolnik if (b <= -27 or b >= -53)}
    fikus_ebat = treugolnik.union(pika_tochenaya)
    hui_drochenie = {a ** 2 + abs(oh_blya) for a in pika_tochenaya
                     for oh_blya in fikus_ebat if a > oh_blya}

    return len(fikus_ebat) - sum([oh_blya * virt
                                  for oh_blya in fikus_ebat
                                  for virt in hui_drochenie])


print(main({99, 3, -86, -50, 50, 83, -73, -40, -2, -97}))
print(main({35, -90, -56, 12, -51, 16, 21, 24, 26}))