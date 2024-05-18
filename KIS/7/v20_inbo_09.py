def main(x):
    x3_up_r = {'TERRA': 1, 'OPAL': 2}
    x3_m1_r = {'TERRA': 3, 'OPAL': 4}
    x3_m2_r = {'TERRA': 5, 'OPAL': 6}
    x3_d_r = {'TERRA': 8, 'OPAL': 9}

    x2_m_m = {'GRACE': 0, 'PAN': x3_up_r[x[3]]}
    x4_m_m = {'JSON': x3_m1_r[x[3]], 'JAVA': x3_m2_r[x[3]],
              'OPAL': 7}
    x2_m_d = {'GRACE': x3_d_r[x[3]], 'PAN': 10}

    x0_l = {'IDL': x2_m_m[x[2]], 'CSON': x4_m_m[x[4]],
            'NIX': x2_m_d[x[2]]}

    x_init = {1965: x0_l[x[0]], 2008: 11}
    return x_init[x[1]]


print(main(['IDL', 1965, 'GRACE', 'OPAL', 'JAVA']))
print(main(['CSON', 2008, 'GRACE', 'OPAL', 'OPAL']))
print(main(['IDL', 1965, 'PAN', 'OPAL', 'JSON']))
print(main(['CSON', 1965, 'GRACE', 'OPAL', 'OPAL']))
print(main(['CSON', 1965, 'GRACE', 'TERRA', 'JAVA']))
