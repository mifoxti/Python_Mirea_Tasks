def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Да': 'Y', 'Нет': 'N'}
    names = []
    dates = []
    numbers = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number = row_tuple[0].split(';')[0]
            formatted_number = (number[0:3] + number[4:7] +
                                number[8:15] + number[16:])
            mail = row_tuple[0].split(';')[1].split('@')[0]
            date = row_tuple[1].replace("-", ".")
            day, month, year = date.split('.')
            new_date = year + '.' + month + '.' + day
            names.append(mail)
            dates.append(new_date)
            numbers.append(formatted_number)
    new_table.append(names)
    new_table.append(dates)
    new_table.append(numbers)
    return new_table


data = [
    ["+7 (635) 493-69-63;sinanz66@gmail.com", "20-04-99"],
    ["+7 (712) 241-17-96;sitan33@yahoo.com", "08-06-03"],
    ["+7 (768) 295-64-99;noruk73@mail.ru", "18-04-01"],
    ["+7 (768) 295-64-99;noruk73@mail.ru", "18-04-01"],
    ["+7 (768) 295-64-99;noruk73@mail.ru", "18-04-01"]
]
from pprint import pprint

pprint(main(data))

