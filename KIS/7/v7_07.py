def main(x):
    x3_t_r = {'XML': 0, 'MIRAH': 1}
    x4_bm_r = {'REBOL': 6, 'EJS': 7, 'STON': 8}
    x4_b_r = {'REBOL': 9, 'EJS': 10, 'STON': 11}

    x0_t_m = {'NGINX': x3_t_r[x[3]], 'ARC': 2, 'IDL': 3}
    x3_b_m = {'XML': x4_bm_r[x[4]], 'MIRAH': x4_b_r[x[4]]}

    x1_t_l = {1974: x0_t_m[x[0]], 2010: 4}
    x1_b_l = {1974: 5, 2010: x3_b_m[x[3]]}

    ini = {1961: x1_t_l[x[1]], 2014: x1_b_l[x[1]]}
    return ini[x[2]]


print(main(['ARC', 2010, 2014, 'XML', 'EJS'])) # = 7
print(main(['NGINX', 1974, 2014, 'MIRAH', 'EJS'])) # = 5
print(main(['NGINX', 2010, 2014, 'MIRAH', 'REBOL'])) # = 9
print(main(['ARC', 2010, 1961, 'XML', 'REBOL'])) # = 4
print(main(['IDL', 1974, 1961, 'XML', 'EJS'])) # = 3