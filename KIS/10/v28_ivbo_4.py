def main(table):
    new_table = []
    unique_rows = set()
    slon = {'false': 'Не выполнено', 'true': 'Выполнено'}
    for string in table:
        row_tuple = tuple(string)
        if string[4] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(int(string[3].rstrip('%'))
                       / 100).ljust(5, '0')
            phone = (string[4].split(';')[0]
                     .replace(' ', '').replace('-', '')
                     .replace('(', '').replace(')', ''))
            yon = slon[string[4].split(';')[1]]
            new_table.append([mark, yon, phone])
    return new_table


from pprint import pprint

pprint(main([[None, None, '96%', '96%', '(103) 023-26-83;false'], [None, None, '91%', '91%', '(630) 689-37-25;true'],
             [None, None, '73%', '73%', '(469) 569-04-59;true'], [None, None, '95%', '95%', '(871) 223-81-50;true'],
             [None, None, '96%', '96%', '(103) 023-26-83;false'], [None, None, '96%', '96%', '(103) 023-26-83;false']]))
