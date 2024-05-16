def main(x):
    x1_t_r = {'SMALI': 1, 'YAML': 2, 'XPROC': 3}
    x1_m_r = {'SMALI': 6, 'YAML': 7, 'XPROC': 8}
    x1_d_r = {'SMALI': 9, 'YAML': 10, 'XPROC': 11}

    x2_t_m = {'VALA': 0, 'ECL': x1_t_r[x[1]]}
    x4_m_m = {'RUST': 5, 'CHUCK': x1_m_r[x[1]],
              'KRL': x1_d_r[x[1]]}

    x0_m_l = {2011: x2_t_m[x[2]], 2002: 4, 1958: x4_m_m[x[4]]}

    dict_init = {'MQL4': x0_m_l[x[0]], 'SAGE': 12, 'XS': 13}

    return dict_init[x[3]]


print(main([2011, 'XPROC', 'VALA', 'MQL4', 'RUST']))  # = 0
print(main([1958, 'YAML', 'VALA', 'SAGE', 'CHUCK']))  # = 12
print(main([2011, 'YAML', 'ECL', 'MQL4', 'KRL']))  # = 2
print(main([2011, 'XPROC', 'ECL', 'XS', 'RUST']))  # = 13
print(main([1958, 'XPROC', 'VALA', 'MQL4', 'CHUCK']))  # = 8
