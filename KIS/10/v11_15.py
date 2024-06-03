def main(table):
    new_table = []
    unique_rows = set()
    slon = {'true': 'Y', 'false': 'N'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            phone = string[1][4:]
            phone = phone[:6] + '-' + phone[6:]
            yon = slon[string[3]]
            name = string[4].split(' ')[1]
            new_table.append([phone, yon, name])
    return new_table


data = [[None, None, None, None, None], [None, '438-326-2069', None, 'false', 'Георгий Фовский'],
        [None, '461-202-8256', None, 'false', 'Данил Рисушяк'], [None, '450-356-2891', None, 'false', 'Филипп Нугев'],
        [None, '005-587-2589', None, 'true', 'Игнат Моляк'], [None, None, None, None, None],
        [None, '005-587-2589', None, 'true', 'Игнат Моляк']]

from pprint import pprint

pprint(main(data))
