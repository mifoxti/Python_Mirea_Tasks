data = [
    ["28-12-03&Ломук А.Д.", "Да", "+75117040588", "+75117040588"],
    ["28-12-03&Ломук А.Д.", "Да", "+75117040588", "+75117040588"],
    ["13-03-99&Торочак В.Г.", "Нет", "+76396862394", "+76396862394"],
    ["28-12-03&Ломук А.Д.", "Да", "+75117040588", "+75117040588"],
    ["27-04-00&Тотиди А.Ч.", "Да", "+78713454548", "+78713454548"]
]


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Да': 'true', 'Нет': 'false'}
    numbers = []
    names = []
    yn = []
    dates = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            date, name = string[0].split('&')
            day, month, year = date.split('-')
            form_date = f'{year}/{month}/{day}'
            form_name = name[:-2]
            y_n = slon[string[1]]
            phone_number = string[2]
            formatted_number = (f"+7({phone_number[2:5]}){phone_number[5:8]}-"
                                f"{phone_number[8:10]}-{phone_number[10:]}")
            dates.append(form_date)
            names.append(form_name)
            yn.append(y_n)
            numbers.append(formatted_number)
    new_table.append(dates)
    new_table.append(names)
    new_table.append(yn)
    new_table.append(numbers)
    return new_table


from pprint import pprint
pprint(main(data))