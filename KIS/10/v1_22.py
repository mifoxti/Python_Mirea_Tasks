def main(table):
    new_table = []
    unique_rows = set()
    mails = []
    fams = []
    yons = []
    slon = {'Нет': 'Не выполнено', 'Да': 'Выполнено'}
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            fio, mail = string[0].split('|')
            fam = fio.split(',')[0]
            mail = mail.replace('[at]', '@')
            yon = slon[string[1]]
            mails.append(mail)
            fams.append(fam)
            yons.append(yon)
    new_table.append(mails)
    new_table.append(fams)
    new_table.append(yons)
    return new_table


data = [['Катянц, А.В.|katanz51[at]yahoo.com', 'Нет', 'Нет'], [None, None, None],
        ['Цевенич, С.Р.|zevenic25[at]yandex.ru', 'Нет', 'Нет'], ['Чифский, Д.О.|cifskij48[at]mail.ru', 'Да', 'Да'],
        ['Риферяк, А.Р.|riferak69[at]rambler.ru', 'Нет', 'Нет']]


from pprint import pprint
pprint(main(data))
