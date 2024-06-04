import re


def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            digits_only = re.sub(r'\D', '', string[0])
            formatted_number = digits_only[-10:]
            formatted_number = (f"({formatted_number[:3]}) "
                                f"{formatted_number[3:6]}-"
                                f"{formatted_number[6:8]}-"
                                f"{formatted_number[8:]}")
            fam, name = string[2].split(' ')
            fname = f"{fam.rstrip(',')} {name[:-2]}"
            mark = str(int(float(string[4]) * 100)) + '%'
            new_table.append([formatted_number, fname, mark])
    return new_table


data = [[None, None, None, None, None], ['+7 442 145-1816', None, 'Вусий, Д.Л.', '0.2', '0.2'],
        ['+7 785 486-1894', None, 'Вачувов, Э.И.', '0.5', '0.5'],
        ['+7 845 809-3371', None, 'Гисоско, П.С.', '0.1', '0.1'], [None, None, None, None, None],
        ['+7 151 510-8502', None, 'Фирко, П.З.', '0.3', '0.3']]
from pprint import pprint

pprint(main(data))
