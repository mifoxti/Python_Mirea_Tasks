def main(table):
    new_table = []
    trans = {'Выполнено': '1', 'Не выполнено': '0'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            parts = string[1].split(', ')
            new_row = [trans[string[0]],
                       f'{parts[1][0]}. {parts[0]}', ''.join(string[2].split(' '))]
            new_table.append(new_row)
    return new_table

input_table = [
    ['Выполнено', 'Нокман, Д.Ф.', '+7 (149) 502-21-44', '+7 (149) 502-21-44'],
    ['Не выполнено', 'Гирикко, Р.Ш.', '+7 (608) 550-54-67', '+7 (608) 550-54-67'],
    ['Не выполнено', 'Кесезяк, М.Г.', '+7 (790) 676-62-54', '+7 (790) 676-62-54'],
    [None, None, None, None],
    ['Выполнено', 'Точко, Д.У.', '+7 (007) 455-61-08', '+7 (007) 455-61-08'],
    ['Выполнено', 'Точко, Д.У.', '+7 (007) 455-61-08', '+7 (007) 455-61-08'],
    [None, None, None, None],
    ['Выполнено', 'Точко, Д.У.', '+7 (007) 455-61-08', '+7 (007) 455-61-08']
]

for row in main(input_table):
    print(row)
