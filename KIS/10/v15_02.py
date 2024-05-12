def main(table):
    new_table = []
    trans = {'Y': 'Выполнено', 'N': 'Не выполнено'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            date = string[0].split('!')[0]
            year, mth, day = date.split('/')
            formated_date = f"{day}/{mth}/{year[2::]}"
            yN = trans[string[0].split('!')[1]]
            name = string[3][:-2]
            new_table.append([yN, formated_date, name])
    return new_table


input_table = [['2002/05/10!Y', None, None, 'Лудак О.И.'],
               ['2001/09/17!N', None, None, 'Руминиди В.Б.'],
               ['2002/06/05!N', None, None, 'Вицонак Н.И.']]


for row in main(input_table):
    print(row)
