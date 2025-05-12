def main(table):
    new_table = []
    trans = {'N': 'false', 'Y': 'true'}
    unique_rows = set()

    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            i, o, f = string[0].split(' ')
            formated_name = f"{i[0]}.{o} {f}"
            yon = trans[string[1]]
            phone = string[2].lstrip('(').replace(') ', '-')
            mark = f"{round(float(string[3]), 2):.2f}"
            new_table.append([formated_name, yon, phone, mark])
    return new_table


from pprint import pprint
pprint(main([['Никита Т. Недберг', 'N', '(931) 519-2044', '0.9918'], ['Святогор Л. Цазян', 'Y', '(670) 189-3310', '0.0160'], ['Тимофей И. Шугич', 'N', '(135) 023-7726', '0.4558'], ['Тимофей И. Шугич', 'N', '(135) 023-7726', '0.4558'], ['Тимофей И. Шугич', 'N', '(135) 023-7726', '0.4558']]))