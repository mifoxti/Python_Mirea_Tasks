def main(table):
    new_table = []
    unique_rows = set()
    numbers = []
    mails = []
    marks = []
    names = []
    for row in table:
        row_tuple = tuple(row)
        if row[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number, mail = row[0].split('!')
            numer = number.split(' ')[1].replace('-', '')
            mail = mail.split('@')[1]
            mark = row[2].ljust(5, '0')
            name = row[3][5:]
            mails.append(mail)
            marks.append(mark)
            names.append(name)
            numbers.append(numer)
    new_table.append(mails)
    new_table.append(marks)
    new_table.append(names)
    new_table.append(numbers)
    return new_table


data = [['(928) 737-79-20!ludinko16@gmail.com', None, '0.37', 'Д.И. Лудинко'],
        ['(380) 071-57-52!tosakberg69@yandex.ru', None, '0.37', 'В.Ш. Тосакберг'],
        ['(380) 071-57-52!tosakberg69@yandex.ru', None, '0.37', 'В.Ш. Тосакберг'],
        ['(811) 289-79-08!kukev47@rambler.ru', None, '0.86', 'Р.З. Кукев'],
        ['(687) 175-67-53!lilezanz80@yahoo.com', None, '0.67', 'В.Т. Лилезянц']]

from pprint import pprint

pprint(main(data))
