from functools import cache


@cache
def lev_dist_ops(str1, str2):
    if not str1:
        return len(str2), ['вставка'] * len(str2)
    if not str2:
        return len(str1), ['удаление'] * len(str1)

    if str1[0] == str2[0]:
        cost = 0
    else:
        cost = 1

    dist_insert, ops_insert = lev_dist_ops(tuple(str1), tuple(str2))
    dist_delete, ops_delete = lev_dist_ops(tuple(str1[1:]), tuple(str2))
    dist_replace, ops_replace = lev_dist_ops(tuple(str1[1:]), tuple(str2[1:]))

    dist_insert += 1
    dist_delete += 1
    dist_replace += cost

    if dist_insert <= dist_delete and dist_insert <= dist_replace:
        return dist_insert, ['вставка'] + ops_insert
    elif dist_delete <= dist_insert and dist_delete <= dist_replace:
        return dist_delete, ['удаление'] + ops_delete
    else:
        return dist_replace, (['замена'] if cost else []) + ops_replace


def lev_dist_gen(str1, str2):
    ops = lev_dist_ops(str1, str2)[1]

    if not ops:
        return "Последовательности уже равны"

    result = []
    x_idx, y_idx = 0, 0

    for op in ops:
        if op == 'вставка':
            result.append(f"x.insert({x_idx}, y[{y_idx}])")
            y_idx += 1
        elif op == 'удаление':
            result.append(f"del x[{x_idx}]")
            x_idx += 1
        elif op == 'замена':
            result.append(f"x[{x_idx}] = y[{y_idx}]")
            x_idx += 1
            y_idx += 1

    return "\n".join(result)


# Пример использования
str1 = 'достаток'
str2 = 'остаточный'
code = lev_dist_gen(list(str1), list(str2))
print(code)
