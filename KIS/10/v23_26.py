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
            date = date[:6] + date[8:]
            new_table.append([number, yon, date, mail])
    return new_table


data = [[None, '(109) 266-6484', '(109) 266-6484', 'да:vekev56[at]rambler.ru', None, '13.12.2000'],
        [None, None, None, None, None, None],
        [None, '(176) 788-4792', '(176) 788-4792', 'да:sisuk35[at]mail.ru', None, '03.04.1999'],
        [None, '(870) 538-1179', '(870) 538-1179', 'да:figobij29[at]gmail.com', None, '14.02.1999']]


from pprint import pprint

pprint(main(data))