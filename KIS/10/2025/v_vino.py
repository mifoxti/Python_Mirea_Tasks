def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            num = string[0].split(') ')[1].split('-')
            f_num = f"{num[0]}-{num[1]}{num[2]}"
            mark, mail = string[1].split('!')

            mark = f"{round(float(mark), 1):.1f}"
            mail = mail.split('[')[0]
            name = string[2].split(' ')[1]
            new_table.append([f_num, mail, mark, name])
    return new_table


from pprint import pprint

data = [['+7 (782) 893-84-48', '0.4713!selezko29[at]yahoo.com', 'Герман Селецко', 'Герман Селецко'],
        ['+7 (651) 430-60-24', '0.2496!aleksej96[at]yahoo.com', 'Алексей Шомук', 'Алексей Шомук'],
        [None, None, None, None], ['+7 (052) 113-83-09', '0.3724!zahar57[at]gmail.com', 'Захар Шодев', 'Захар Шодев'],
        ['+7 (729) 999-38-53', '0.1617!stanislav2[at]yahoo.com', 'Станислав Цагиди', 'Станислав Цагиди'],
        ['+7 (729) 999-38-53', '0.1617!stanislav2[at]yahoo.com', 'Станислав Цагиди', 'Станислав Цагиди'],
        ['+7 (729) 999-38-53', '0.1617!stanislav2[at]yahoo.com', 'Станислав Цагиди', 'Станислав Цагиди']]
pprint(main(data))
