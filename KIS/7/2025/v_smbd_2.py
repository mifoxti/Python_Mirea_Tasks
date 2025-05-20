def main(x):
    x_3_top = {'CSS': 0, 'SLASH': 1}
    x_3_mid_top = {'CSS': 2, 'SLASH': 3}
    x_1_mid_mid = {'RUST': 4, 'COOL': 5}
    x_3_mid_bottom = {'CSS': 6, 'SLASH': 7}
    x_3_bottom = {'CSS': 9, 'SLASH': 10}

    x_2_top = {'CLICK': x_3_top[x[3]],
               'CSON': x_3_mid_top[x[3]],
               'RUST': x_1_mid_mid[x[3]], }
    x_2_mid = {'CLICK': x_3_mid_bottom[x[3]],
               'CSON': 8,
               'RUST': x_3_bottom[x[3]]}

    x_init = {2012: x_2_top[x[2]],
              2009: x_2_mid[x[2]],
              1975: 11}

    return x_init[x[0]]
