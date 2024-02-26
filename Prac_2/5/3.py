from functools import cache


@cache
def lev_dist(str1, str2):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    if str1[0] == str2[0]:
        cost = 0
    else:
        cost = 1

    return min(
        lev_dist(str1[1:], str2) + 1,
        lev_dist(str1, str2[1:]) + 1,
        lev_dist(str1[1:], str2[1:]) + cost
    )


result = lev_dist('столб', 'слон')
print(result)
