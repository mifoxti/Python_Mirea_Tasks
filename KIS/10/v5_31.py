def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Да': 'Y', 'Нет': 'N'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] != None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number = row_tuple[1].split('|')[0]
            formatted_number = "{:.3f}".format(float(number))
            yN = slon[row_tuple[1].split('|')[1]]
            name = row_tuple[2]
            formatted_name = name[0:2] + name[5::]
            new_table.append([yN, formatted_number, formatted_name])
    return sorted(new_table, key=lambda x: x[2])


input_table = data = [
    [None, "0.9|Да", "С.Ч. Чивиди", None, "С.Ч. Чивиди"],
    [None, "0.5|Нет", "Я.З. Бедяк", None, "Я.З. Бедяк"],
    [None, "0.9|Нет", "А.Д. Декко", None, "А.Д. Декко"],
    [None, "0.7|Да", "С.Е. Бедишич", None, "С.Е. Бедишич"],
    [None, "0.7|Да", "С.Е. Бедишич", None, "С.Е. Бедишич"],
    [None, "0.7|Да", "С.Е. Бедишич", None, "С.Е. Бедишич"]
]
form = main(input_table)
from pprint import pprint
pprint(form)
