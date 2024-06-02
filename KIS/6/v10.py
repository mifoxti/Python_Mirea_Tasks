from math import ceil


def main(M):
    Phi = {6 * mu + abs(mu) for mu in M if mu > -92}
    N = {mu for mu in M if not (-74 <= mu < 38)}
    oriel = {nu * phu for nu in N for phu in Phi if nu <= phu}
    cartesian_product_size = len([ogo * phu for ogo in oriel
                                  for phu in Phi])
    sum_value = sum(ceil(phi / 8) - abs(ogo) for phi in Phi
                    for ogo in oriel)
    beta = cartesian_product_size - sum_value
    return beta


# Test examples
example1 = {-96, -30, 99, 4, 71, -87, 47, -14, 87, 57}
example2 = {-95, 5, -23, 76, 77, 12, 55, 92, -99, 30}

print(f"main({example1}) = {main(example1)}")
print(f"main({example2}) = {main(example2)}")
