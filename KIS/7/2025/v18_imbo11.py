def main(x):
    x1_top_end = {2020: 0,
                  1974: 1}
    x1_topmid_end = {2020: 2,
                     1974: 3}
    xo_topbot_end = {'RAML': 4,
                     'YACC': 5,
                     'DART': 6}

    x0_bottop_end = {'RAML': 8,
                     'YACC': 9,
                     'DART': 10}

    x3_top_mid = {'POD': x1_top_end[x[1]],
                  'XC': x1_topmid_end[x[1]],
                  'EQ': xo_topbot_end[x[0]]}
    x3_bot_mid = {'POD': x0_bottop_end[x[0]],
                  'XC': 11,
                  'EQ': 12}

    x2 = {1968: x3_top_mid[x[3]],
          1973: 7,
          1965: x3_bot_mid[x[3]], }
    return x2[x[2]]
