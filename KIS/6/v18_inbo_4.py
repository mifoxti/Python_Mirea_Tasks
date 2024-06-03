def main(delta):
    obig = {delta for delta in delta if delta > -46}
    podkova = {e - e % 2 for e in obig if -89 < e <= 1}
    fi = {abs(w) - 3 * w for w in podkova if -67 < w <= 72}
    ZOV = {4 * b + e % 3 for b in delta for e in obig if b >= e}
    orki = {c ** 2 - w ** 3 for c in ZOV for w in podkova if c >= w}
    return len(orki) + sum([abs(ofi) for ofi in fi])


print(main({-32, 66, -56, -54, -81, -78, 50, -75, -2, -66}))
print(main({96, -31, -30, -60, -90, -57, -50, -11, 27}))
