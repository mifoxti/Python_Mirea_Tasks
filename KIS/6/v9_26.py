import math
import operator


def main(T):
    ogo = {abs(teta) for teta in T if teta < -26 or teta > 7}
    N = {math.ceil(teta / 5) for teta in T
         if operator.xor(teta <= 43, teta >= -25)}
    fontan = {ν for ν in N if ν < 79 or ν > -38}
    cartesian_product = [(o, ν) for o in ogo for ν in fontan]
    chi = len(cartesian_product) + sum(math.ceil(o / 6)
                                       + math.floor(ν / 6)
                                       for o, ν in cartesian_product)
    return chi


# Example usage
print(main({34, -92, -27, -25, -56, 10, 81, -78, 50, -74}))  # should return 598
print(main({-86, -82, -84, -80, -13, 17, 58, 21, -71, -99}))  # should return 374
