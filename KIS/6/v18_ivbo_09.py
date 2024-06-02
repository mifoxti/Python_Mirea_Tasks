from operator import xor


def main(A):
    ibat = {6 * amin - 2 * amin for amin in A if -73 <= amin < 46}
    trezubec = {i for i in ibat if (xor(i > -41, i <= 2))}
    obig = {amin * i for amin in A for i in ibat if amin <= i}
    nigger = {2 * o for o in obig if xor(o > -24, o < 57)}
    hi = {vi for vi in trezubec if -21 <= vi < 91}

    return (len([n * h for n in nigger for h in hi])
            - sum([vi * ni for vi in nigger for ni in hi]))


print(main({-62, 70, 38, 10, -80, -14, 19, -4, 95, 63}))  # = -5775818
print(main({1, 66, -58, 38, -19, -50, -49, -16, -47, 85}))  # = 67248
