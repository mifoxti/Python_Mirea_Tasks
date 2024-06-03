def main(agar):
    xin = {a ** 2 + 4 * a for a in agar if not -43 < a < 56}
    ogo = {a for a in agar if -80 < a < 84}
    obig = {e ** 2 for e in ogo if e > -8}

    pe = 1
    for x in xin:
        for o in obig:
            pe *= (x % 3) - (o % 2)
    return sum(xin) + pe

print(main({2, 68, 37, 73, -15, 54, -40, 89, 58, 29}))
print(main({-60, -37, 41, -21, 16, 88, -71, 26, 91, -3}))