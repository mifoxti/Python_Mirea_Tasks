def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            name = string[0].split(' ')
            fname = f"{name[1]} {name[0][:2]}"
            mark1, date = string[3].split('!')
            percent = round(float(mark1) * 100)
            percent_str = f"{percent}%"
            day, mont, year = date.split('/')
            fdate = f"{year}/{mont}/{day}"
            new_table.append([fname, percent_str, fdate])
    sorted_table = sorted(new_table, key=lambda x: x[0])
    return sorted_table


data = [['В.С. Рарерян', None, 'В.С. Рарерян', '0.3895!03/08/24'],
        ['Д.Г. Гицогиди', None, 'Д.Г. Гицогиди', '0.5262!04/07/19'], [None, None, None, None],
        ['Т.Ф. Гобко', None, 'Т.Ф. Гобко', '0.4715!00/02/21'], ['А.Ц. Сифий', None, 'А.Ц. Сифий', '0.6386!01/02/06']]

from pprint import pprint
pprint(main(data))