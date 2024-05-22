def main(x):
    x4_m_r = {2019: 1, 1964: 2, 2013: 3}
    x4_d_r = {2019: 4, 1964: 5, 2013: 6}
    x1_m_m = {1987: 0, 1980: x4_m_r[x[4]], 1988: x4_d_r[x[4]]}
    x2_m_l = {'ATS': x1_m_m[x[1]], 'HLSL': 7}
    x0 = {'PIC': x2_m_l[x[2]], 'CHUCK': 8, 'VUE': 9}
    return x0[x[0]]


print(main(['PIC', 1987, 'HLSL', 'EQ', 2013]))  # = 7
print(main(['VUE', 1980, 'HLSL', 'SCSS', 2013]))  # = 9
print(main(['PIC', 1987, 'ATS', 'SCSS', 1964]))  # = 0
print(main(['PIC', 1980, 'ATS', 'SCSS', 1964]))  # = 2
print(main(['CHUCK', 1988, 'HLSL', 'EQ', 2019]))  # = 8
