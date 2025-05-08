def main(x):
    x0_centr_top = {'CLICK': 0, 'NIT': 1, 'BISON': 2}

    x0_last_top = {'CLICK': 3, 'NIT': 4, 'BISON': 5}
    x3_last_mid = {1966: 6, 1990: 7, 1959: 8}
    x0_last_bottom = {'CLICK': 9, 'NIT': 10, 'BISON': 11}

    x2_center_mid = {1997: x0_last_top[x[0]],
                     1969: x3_last_mid[x[3]],
                     1966: x0_last_bottom[x[0]]}

    x4_pred = {'XML': x0_centr_top[x[0]],
               'KICAD': x2_center_mid[x[2]],
               'TOML': 12}

    x1 = {'LEAN': x4_pred[x[4]],
          'IO': 13}
    return x1[x[1]]


print(main(['CLICK', 'LEAN', 1966, 1959, 'TOML']) )
print(main(['NIT', 'LEAN', 1969, 1990, 'XML']))
print(main(['BISON', 'IO', 1997, 1966, 'TOML']) )
print(main(['BISON', 'LEAN', 1997, 1990, 'KICAD']))
print(main(['CLICK', 'LEAN', 1997, 1990, 'XML']))