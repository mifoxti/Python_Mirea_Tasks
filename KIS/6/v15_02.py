def main(k):
    trezubec = {ke for ke in k if ke > -91}
    x = {ke ** 3 - 6 * ke for ke in k if not (-27 < ke < 35)}
    fi = {u * ix for u in trezubec for ix in x if u <= ix}
    m = {abs(ix) + ix % 2 for ix in x if ix not in range(-71, -25)}
    Sigma = sum(o % 2 + uu % 2 for o in fi for uu in m)
    product_l_A = len([(lll * a) for a in m for lll in fi])
    return product_l_A - Sigma


print(main({-31, 68, -58, -57, -88, 41, 74, 14, 49, 58}))
print(main({-31, 35, -92, 8, 74, 43, 15, -47, -12, -3}))
