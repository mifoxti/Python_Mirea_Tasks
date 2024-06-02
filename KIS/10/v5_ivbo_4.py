def main(table):
    new_table = []
    trans = {'Не выполнено': 'нет', 'Выполнено': 'да'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(round(float(string[0]), 1))
            yon = trans[string[1].split('&')[0]]
            date = string[1].split('&')[1].replace('-', '/')
            new_table.append([mark, date, yon])
    return new_table
