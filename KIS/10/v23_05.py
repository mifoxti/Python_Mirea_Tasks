def main(table):
    new_table = []
    unique_rows = set()
    numbers = []
    names = []
    mails = []
    dates = []
    for row in table:
        row_tuple = tuple(row)
        if row[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail, number = row[1].split(':')
            number = number.replace('-', '')
            name, ini, fam = row[2].split()
            fname = f"{name} {fam}"
            mail = mail.replace('[at]', '@')
            date = row[3].replace('/', '.')
            numbers.append(number)
            names.append(fname)
            mails.append(mail)
            dates.append(date)
    new_table.append(numbers)
    new_table.append(names)
    new_table.append(mails)
    new_table.append(dates)
    return new_table


from pprint import pprint

data = [[None, 'fetebic81[at]rambler.ru:345-396-5227', 'Рамиль Г. Фетебич', '27/04/99', '27/04/99'],
        [None, 'vitalij20[at]yahoo.com:025-219-1196', 'Виталий А. Чезяк', '25/03/01', '25/03/01'],
        [None, None, None, None, None], [None, None, None, None, None],
        [None, 'matvej87[at]yahoo.com:705-005-1023', 'Матвей Е. Цечиди', '13/05/99', '13/05/99']]

pprint(main(data))
