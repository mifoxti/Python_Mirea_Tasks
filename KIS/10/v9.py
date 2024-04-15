def main(table):
    new_table = []
    trans = {'Выполнено': 'Да', 'Не выполнено': 'Нет'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)

            date = string[0].split('.')
            date_fracted = f'{date[2]}.{date[1]}.{date[0]}'

            check = trans[string[1]]

            mark = string[3] + '0'

            surname = string[6].split(' ')[1]

            new_table.append([date_fracted, check, mark, surname])

    return new_table


input_table = [['2003.07.07', 'Не выполнено', None, '0.44', None, 'Не выполнено', 'Т.Н. Тагко'], ['2000.01.04', 'Не выполнено', None, '0.04', None, 'Не выполнено', 'В.М. Расий'], ['2001.08.25', 'Не выполнено', None, '0.75', None, 'Не выполнено', 'Я.С. Цодесев'], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None], ['2001.08.25', 'Не выполнено', None, '0.75', None, 'Не выполнено', 'Я.С. Цодесев']]


for row in main(input_table):
    print(row)
