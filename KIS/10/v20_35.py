def main(table):
    new_table = []
    unique_rows = set()
    slon = {'да': '1', 'нет': '0'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yon, number = string[1].split('&')
            yon = slon[yon]
            number = number.replace(' ', '-')
            day, mont, year = string[2].split('-')
            fdate = f'{year}/{mont}/{day}'
            new_table.append([number, yon, fdate])
    return new_table
