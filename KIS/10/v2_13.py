def main(table):
    new_table = []
    trans = {'1': 'Да', '0': 'Нет'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yN = trans[string[0].split('!')[0]]
            mark = str(round(float(string[0].split('!')[1]), 2))
            date = string[1].replace('/', '.')
            if len(mark) < 4:
                mark += '0'
            new_table.append([yN, mark, date])
    return new_table


print(round(float('0.329'), 2))