def format_phone(phone_str):
    a, b, c = phone_str.split('-')
    return f"{b}-{c[:2]}-{c[2:]}"


def format_name(name_str):
    name, date = name_str.split(';')
    d, m, y = date.split('/')
    f_date = f"{y}-{m}-{d}"
    n, o, f = name.split(' ')
    f_name = f"{n[0]}.{o} {f}"
    return f_date, f_name


def format_email(email_str):
    return email_str.replace('@', '[at]')


def main(table):
    new_table = []
    unique_rows = set()

    for row in table:
        row_tuple = tuple(row)
        if not row[0] or row_tuple in unique_rows:
            continue

        unique_rows.add(row_tuple)

        phone = format_phone(row[0])
        date, name = format_name(row[1])
        email = format_email(row[2])

        new_table.append([phone, date, email, name])
    sorted_table = sorted(new_table, key=lambda x: x[0])
    return sorted_table


from pprint import pprint

data = [[None, None, None], ['119-197-9258', 'Егор Е. Ривунич;10/02/99', 'rivunic68@rambler.ru'],
        ['850-608-3463', 'Захар Г. Шориди;01/09/02', 'soridi88@gmail.com'],
        ['138-594-1360', 'Тихон М. Рузберг;28/03/01', 'ruzberg92@mail.ru'],
        ['476-808-9134', 'Альберт К. Мубич;17/04/02', 'al_bert13@yahoo.com']]
pprint(main(data))
