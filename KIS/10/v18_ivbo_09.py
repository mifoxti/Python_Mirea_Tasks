def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            i, o, f = string[0].split('!')[0].split(' ')
            formated_name = f'{f}, {i[0]}.{o}'
            year, month, day = string[0].split('!')[1].split('-')
            formated_date = f'{day}/{month}/{year}'
            phone = string[1]
            form_number = (phone[:2] + ' ' + phone[2:5] + ' '
                           + phone[5:8] + '-' + phone[8:10]
                           + '-' + phone[10:])
            new_table.append([formated_date, form_number, formated_name])
    return new_table


data = [['Денис З. Тишонман!2002-01-20', '+78670317046', '+78670317046'], [None, None, None],
        ['Артур И. Шавизли!2001-05-01', '+76495339178', '+76495339178'], [None, None, None],
        ['Станислав И. Ноцадли!1999-08-23', '+70641197792', '+70641197792'],
        ['Тамерлан У. Гиниди!2000-01-13', '+71165133175', '+71165133175']]

from pprint import pprint
pprint(main(data))
