from math import ceil


def main(ppp):
    ttt = {p % 3 - ceil(p / 3) for p in ppp if p > 58}
    alpha = {t - t % 2 for t in ttt if -72 < t <= 73}
    hypotesis = {4 * p - p for p in ppp if -31 <= p < 89}
    li = {e ** 2 - e for e in hypotesis if (e <= 46 or e >= -45)}
    proiz = 1
    for a in alpha:
        proiz *= abs(a)
    product_l_A = len([(lll * a) for a in alpha for lll in li])
    return product_l_A - proiz


print(main({-27, 6, 43, -45, 52, 85, 54, 62, 95}))
print(main({-31, -60, 5, 4, -22, -84, 46, 81, -67}))
