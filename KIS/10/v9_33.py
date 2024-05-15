data = [
    ["+7(172)854-52-70", "Иван Р. Рабевич", "true", "true"],
    ["+7(596)411-49-01", "Ростислав Б. Вавенский", "false", "false"],
    ["+7(113)296-67-97", "Владислав Ч. Лисишов", "false", "false"]
]



def main(table):
    new_table = []
    unique_rows = set()
    slon = {'true': 'да', 'false': 'нет'}
    numbers = []
    names = []
    yn = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number = string[0].replace('(', ' ').replace(')', ' ')
            name = string[1].split(' ')[0] + ' ' + string[1].split(' ')[2]
            yesorno = slon[string[2]]
            numbers.append(number)
            names.append(name)
            yn.append(yesorno)
    new_table.append(numbers)
    new_table.append(names)
    new_table.append(yn)
    return new_table


from pprint import pprint

pprint(main(data))
