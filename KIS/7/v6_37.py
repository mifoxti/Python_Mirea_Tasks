def main(x):
    x2_t_r = {'GLYPH': 0, 'LASSO': 1, 'SAGE': 2}
    x2_m_r = {'GLYPH': 3, 'LASSO': 4, 'SAGE': 5}
    x4_b_r = {'LOGOS': 6, 'M4': 7}

    x3_m_m = {'RAGEL': x2_t_r[x[2]], 'BRO': x2_m_r[x[2]],
              'MIRAH': x4_b_r[x[4]]}

    x0_m_l = {'SVG': x3_m_m[x[3]], 'M': 8,
              'COBOL': 9}

    x1_m_l = {2003: x0_m_l[x[0]], 2020: 10}

    return x1_m_l[x[1]]


print(main(['M', 2003, 'LASSO', 'RAGEL', 'LOGOS']))
print(main(['COBOL', 2020, 'SAGE', 'BRO', 'M4']))
print(main(['COBOL', 2003, 'GLYPH', 'MIRAH', 'LOGOS']))
print(main(['SVG', 2003, 'GLYPH', 'MIRAH', 'LOGOS']))
print(main(['SVG', 2003, 'LASSO', 'BRO', 'LOGOS']))