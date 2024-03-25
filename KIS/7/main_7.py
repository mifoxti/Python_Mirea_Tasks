x = {(1976, 2017): 0,
     (1975, 2017): 1,
     (1971, 2017): 2,
     (1976, 2019): 4,
     (1975, 2019): 5,
     (1971, 2019): 6,
     (2017, 1975): 8,
     (1980, 1975): 9,
     (2019, 1975): 10}


def main(arr):
    if arr[2] == 2015:
        return 13
    elif arr[2] == 1991:
        return 12
    else:
        if arr[3] == 1981:
            if arr[1] == 1980:
                return 3
        else:
            if arr[0] == 1976:
                return 7
            elif arr[0] == 1971:
                return 11
            else:
                return
            arr.pop(1)
        arr = tuple(arr)
        return x[arr]
