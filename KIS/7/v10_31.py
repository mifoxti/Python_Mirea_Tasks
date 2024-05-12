def main(x):
    dict_x3_up = {'M': 0, 'COBOL': 1, 'ABAP': 2}
    dict_x2_mid = {'LSL': 4, 'TLA': 5}
    dict_x3_down = {'M': 8, 'COBOL': 9, 'ABAP': 10}

    dict_x1_center = {'JULIA': dict_x3_up[x[3]], 'RAML': 3,
                      'DYLAN': dict_x2_mid[x[2]]}
    dict_x1_center_dowm = {'JULIA': 6, 'RAML': 7,
                           'DYLAN': dict_x3_down[x[3]]}
    dict_init = {'RAML': dict_x1_center[x[1]],
                 'C': dict_x1_center_dowm[x[1]], 'LESS': 11}

    return dict_init[x[0]]


print(main(['LESS', 'JULIA', 'TLA', 'M']))
print(main(['C', 'JULIA', 'LSL', 'M']))
print(main(['C', 'DYLAN', 'LSL', 'ABAP']))
print(main(['RAML', 'JULIA', 'LSL', 'COBOL']))
print(main(['C', 'RAML', 'TLA', 'M']))
