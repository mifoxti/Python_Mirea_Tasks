from math import ceil, floor


def main(H):
    trezubec = {ceil(n / 3) for n in H if -20 <= n < 77}
    t_big = {abs(n) + n % 3 for n in H if ((n >= -10) ^ (n <= 37))}
    ogo = {v ** 2 for v in trezubec if v >= -89}
    delta = {floor(o/9) + ceil(o/9) for o in ogo if o < 31}
    a_big = t_big | ogo
    sigma = sum([ceil(a / 7) for a in a_big])
    product_result = 1
    for num in delta:
        product_result *= num
    return sigma + product_result


print(main({-29, 7, 75, 44, 80, 52, -72, 57, -6, 28})) # = 305
print(main({3, -60, 4, 39, -56, 74, -49, 17, -77, 22})) # = 189