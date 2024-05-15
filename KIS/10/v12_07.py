def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail = string[0].split('|')[0].replace('@', '[at]')
            mark = string[2] + '00'
            zo = '1' if string[0].split('|')[1] == 'true' else '0'
            new_table.append([zo, mail, mark])
    return new_table
