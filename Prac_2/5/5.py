from f4 import lev_dist_ops


def lev_dist_gen(str1, str2):
    ops = lev_dist_ops(tuple(str1), tuple(str2))[1]

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
