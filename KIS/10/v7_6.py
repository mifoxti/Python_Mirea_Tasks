def main(table):
    new_table = []
    slon = {'Да': '1', 'Нет': '0'}
    unique_rows = set()
    names = []
    mails = []
    yons = []
    dates = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            fam, ini = string[0].split(' ')
            fname = f"{ini[:-2]} {fam}"
            mail = string[1].split('@')[1]
            yon = slon[string[3]]
            day, month, year = string[4].split('-')
            fdate = f"{year}.{month}.{day}"
            names.append(fname)
            mails.append(mail)
            yons.append(yon)
            dates.append(fdate)
    new_table.append(names)
    new_table.append(mails)
    new_table.append(yons)
    new_table.append(dates)
    return new_table


data = [['Вомешов Д.В.', 'vomesov16@yandex.ru', 'Вомешов Д.В.', 'Да', '14-07-99'],
        ['Соладский В.К.', 'soladskij97@yahoo.com', 'Соладский В.К.', 'Да', '26-11-00'],
        ['Демко Т.Т.', 'demko56@rambler.ru', 'Демко Т.Т.', 'Да', '10-10-00'],
        ['Демко Т.Т.', 'demko56@rambler.ru', 'Демко Т.Т.', 'Да', '10-10-00'],
        ['Демко Т.Т.', 'demko56@rambler.ru', 'Демко Т.Т.', 'Да', '10-10-00']]

from pprint import pprint
pprint(main(data))
