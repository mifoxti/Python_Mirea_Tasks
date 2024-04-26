def main(x):
    dict_x2_up = {2005: 0, 1985: 1}
    dict_x2_down = {2005: 2, 1985: 3}

    dict_x1_up = {2008: 5, 1985: 6, 1977: 7}
    dict_x1_down = {2008: 8, 1985: 9, 1977: 10}

    dict_x1_mid = {2008: dict_x2_up[x[2]],
                   1985: dict_x2_down[x[2]], 1977: 4}
    dict_x2_mid = {2005: dict_x1_up[x[1]],
                   1985: dict_x1_down[x[1]]}

    dict_init = {"C++": dict_x1_mid[x[1]],
                 "SWIFT": dict_x2_mid[x[2]], "XC": 11}

    return dict_init[x[0]]


print(main(['XC', 1977, 1985, 'DM']))  # = 11