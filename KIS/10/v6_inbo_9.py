def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(round(float(string[2]), 1))
            number = string[1].replace(' ', '-')
            yaer = string[3].split('#')[0].split('.')[2]
            name = string[3].split('#')[1][:-2]
            new_table.append([number, mark, yaer, name])
    return new_table


print(round(float('0.329'), 2))
