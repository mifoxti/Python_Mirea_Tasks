def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Выполнено': 'Y', 'Не выполнено': 'N'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] != None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(float(string[0].rstrip('%'))
                       / 100).ljust(5, '0')
            yon = slon[string[1]]
            mail = string[2].replace('[at]', '@')
            new_table.append([mark, yon, mail])
    return new_table


print(str(float('48%'.rstrip('%')) / 100).ljust(5, '0'))
