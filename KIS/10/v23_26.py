def main(table):
    new_table = []
    unique_rows = set()
    slon = {'да': 'Выполнено', 'нет': 'Не выполнено'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number = string[1].split(' ')[1]
            yon, mail = string[3].split(':')
            yon = slon[yon]
            mail = mail.split(']')[1]
            date = string[5].replace('.', '/')
            new_table.append([number, yon, date, mail])
    return new_table
