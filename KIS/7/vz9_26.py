def main(x):
    x0_t_r = {2018: 0, 1969: 1}
    x3_mt_r = {1986: 3, 1961: 4}
    x3_m_r = {1986: 5, 1961: 6}
    x0_b_r = {2018: 9, 1969: 10}

    x1_m_l = {1963: x0_t_r[x[0]], 2008: 2,
              1965: x3_mt_r[x[3]]}
    x1_m_bl = {1963: x3_m_r[x[3]],
               2008: 7,
               1965: 8}
    x3_b_l = {1986: x0_b_r[x[0]],
              1961: 11}

    ini = {'EAGLE': x1_m_l[x[1]],
           'JAVA': x1_m_bl[x[1]],
           'SCSS': x3_b_l[x[3]]}
    return ini[x[2]]


print(main([1969, 2008, 'EAGLE', 1961]))
print(main([1969, 1963, 'EAGLE', 1961]))
print(main([2018, 1965, 'EAGLE', 1961]))
print(main([1969, 2008, 'JAVA', 1986]))
print(main([2018, 2008, 'SCSS', 1961]))
