def main(table):
    new_table = []
    unique_rows = set()
    mails = []
    dates = []
    names = []
    numbers = []
    for row in table:
        row_tuple = tuple(row)
        if row[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail = row[0].split('@')[0]
            data = row[1].replace('-', '/')
            ini, fam = row[2].split(' ')
            fname = f"{fam} {ini[:2]}"
            phone_number = row[3]
            if phone_number.startswith('+7'):
                phone_number = phone_number[2:]
            formatted_number = (f"{phone_number[:3]}"
                                f"-{phone_number[3:6]}-{phone_number[6:]}")
            mails.append(mail)
            dates.append(data)
            names.append(fname)
            numbers.append(formatted_number)
    new_table.append(mails)
    new_table.append(dates)
    new_table.append(names)
    new_table.append(numbers)
    return new_table

from pprint import pprint

data = [['bekak67@rambler.ru', '04-01-00', 'Г.Г. Бекак', '+73570011780'],
        ['safusidi87@yahoo.com', '14-05-01', 'К.Е. Шафусиди', '+71677221121'],
        ['bagonov56@yahoo.com', '27-05-01', 'Г.Г. Багонов', '+70077828535'],
        ['tasizak60@rambler.ru', '16-06-04', 'И.М. Тасизак', '+72187663541'],
        ['bagonov56@yahoo.com', '27-05-01', 'Г.Г. Багонов', '+70077828535'],
        ['bagonov56@yahoo.com', '27-05-01', 'Г.Г. Багонов', '+70077828535']]

data2 = [['covskij75@rambler.ru', '19-10-03', 'Е.Д. Човский', '+77419906282'],
         ['covskij75@rambler.ru', '19-10-03', 'Е.Д. Човский', '+77419906282'],
         ['lisanz43@yahoo.com', '11-07-02', 'М.Л. Лишянц', '+76447730591'],
         ['losivin59@rambler.ru', '24-07-02', 'М.Ф. Лосивин', '+72548598256'],
         ['covskij75@rambler.ru', '19-10-03', 'Е.Д. Човский', '+77419906282']]

pprint(main(data))
pprint(main(data2))
