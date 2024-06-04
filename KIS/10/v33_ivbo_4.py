import re


def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            digits_only = re.sub(r'\D', '', string[3])
            formatted_number = digits_only[-10:]
            formatted_number = (f"({formatted_number[:3]}) "
                                f"{formatted_number[3:6]}-"
                                f"{formatted_number[6:]}")
            mark = str(float(string[2].rstrip('%')) / 100).ljust(5, '0')
            mark = mark.ljust(5, '0')
            fam = string[1].split(' ')[1]
            new_table.append([fam, mark, formatted_number])
    return new_table


data = [[None, 'Влад Колидук', '23%', '+79926569229', '+79926569229'],
        [None, 'Богдан Лузулян', '77%', '+73598373670', '+73598373670'],
        [None, 'Семен Зигибяк', '10%', '+75137860417', '+75137860417']]
from pprint import pprint

pprint(main(data))

data2 = [[None, 'Мирослав Векицяк', '70%', '+74376769698', '+74376769698'], [None, 'Марк Казко', '9%', '+73606293808', '+73606293808'], [None, 'Григорий Бизак', '55%', '+74305502902', '+74305502902']]

pprint(main(data2))