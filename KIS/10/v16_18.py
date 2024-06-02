import re


def main(table):
    new_table = []
    unique_rows = set()
    slovar = {'1': 'Y', '0': 'N'}

    for row in table:
        row_tuple = tuple(row)
        if row[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            digits_only = re.sub(r'\D', '', row[0])
            formatted_number = digits_only[-10:]
            formatted_number = (f"{formatted_number[:3]}"
                                f"-{formatted_number[3:6]}"
                                f"-{formatted_number[6:]}")
            name, fam = row[1].split(' ')
            fname = f"{fam} {name}"
            mark = str(round(float(row[2]), 1))
            new_table.append([formatted_number, fname, mark])
    return new_table


from pprint import pprint
pprint(main(data))