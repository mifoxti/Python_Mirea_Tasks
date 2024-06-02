data = [['Ростислав Д. Фалев', 'rostislav18[at]rambler.ru&33%'],
        ['Виктор И. Рушук', 'viktor55[at]yahoo.com&23%'],
        ['Тимофей Т. Дикук', 'timofej56[at]mail.ru&45%'],
        ['Тимофей Т. Дикук', 'timofej56[at]mail.ru&45%'],
        ['Тимофей Т. Дикук', 'timofej56[at]mail.ru&45%'],
        ['Павел У. Сатиди', 'satidi25[at]yahoo.com&66%']]


def main(table):
    new_table = []
    name = []
    mail = []
    percents = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            f, i, o = string[0].split(' ')
            form_name = f"{o} {f}"
            asdress = string[1].split('&')[0].split('[')[0]
            mark = str(int(string[1].split('&')[1].rstrip('%')) / 100)
            if len(mark) < 4:
                mark += '0'
            name.append(form_name)
            mail.append(asdress)
            percents.append(mark)
    new_table.append(name)
    new_table.append(percents)
    new_table.append(mail)
    return new_table


from pprint import pprint
pprint(main(data))