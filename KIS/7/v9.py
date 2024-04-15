def main(x):
    dict0 = {1992: 0, 1987: 1, 1967: 2}
    dict0_down = {1992: 3, 1987: 4, 1967: 5}
    dictx4 = {'NSIS': dict0[x[0]], 'ROUGE': dict0_down[x[0]], 'COOL': 6}
    dict1x3 = {1966: dictx4[x[4]], 1971: 7, 1978: 8}
    dictx0 = {1992: 9, 1987: 10, 1967: 11}
    dict_init = {'SAS': dict1x3[x[3]], 'INI': dictx0[x[0]]}
    return dict_init[x[1]]

print(main([1987, 'SAS', 'M4', 1966, 'ROUGE']))  # Ожидаемый результат: 13
print(main([1992, 'INI', 'M4', 1966, 'COOL']))  # Ожидаемый результат: 12
print(main([1967, 'SAS', 'M4', 1978, 'COOL']))  # Ожидаемый результат: 5
print(main([1967, 'INI', 'ZIMPL', 1966, 'ROUGE']))  # Ожидаемый результат: 6
print(main([1992, 'SAS', 'SLIM', 1971, 'ROUGE']))  # Ожидаемый результат: 3