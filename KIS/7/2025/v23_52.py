def main(x):
    dict_x2_up = {'FLUX': 0, 'NUMPY': 1, 'MQL5': 2}
    dict_x2_midl = {'FLUX': 3, 'NUMPY': 4, 'MQL5': 5}
    dict_x2_bottom = {'FLUX': 7, 'NUMPY': 8, 'MQL5': 9}

    dict_x1_up = {1963: dict_x2_up[x[2]], 1982: dict_x2_midl[x[2]],
                  1971: 6}
    dict_x1_midl = {1963: dict_x2_bottom[x[2]], 1982: 10,
                    1971: 11}

    dict_x0 = {1963: dict_x1_up[x[1]], 2020: dict_x1_midl[x[1]],
               2019: 12}
    return dict_x0[x[0]]


def test_main():
    assert main([2020, 1982, 'NUMPY', 1973]) == 10
    assert main([2020, 1971, 'NUMPY', 1995]) == 11
    assert main([2020, 1963, 'NUMPY', 1995]) == 8
    assert main([2019, 1982, 'MQL5', 1973]) == 12
    assert main([2020, 1963, 'FLUX', 1973]) == 7
    print("All tests passed!")


test_main()
