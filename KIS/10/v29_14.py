data = [
    ['0.4', '0.4', 'N', '+7 383 518-7177', '14/08/2002'],
    ['0.3', '0.3', 'N', '+7 062 790-1750', '07/02/2000'],
    ['0.7', '0.7', 'Y', '+7 191 727-1934', '03/12/1999'],
    ['0.7', '0.7', 'Y', '+7 191 727-1934', '03/12/1999'],
    ['0.7', '0.7', 'Y', '+7 191 727-1934', '03/12/1999'],
    ['0.5', '0.5', 'Y', '+7 087 357-5330', '21/08/2000']
]


def main(table):
    new_table = []
    trans = {'Y': '1', 'N': '0'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = row_tuple[0] + '0'
            yN = trans[row_tuple[2]]
            phone_number = row_tuple[3]
            parts = phone_number.split()
            country_code = parts[0]
            city_code = parts[1]
            number_part1 = parts[2].split('-')[0]
            number_part2 = parts[2].split('-')[1]
            date_str = row_tuple[4]
            formatted_number = (f"{country_code} ({city_code}) {number_part1}"
                                f"-{number_part2[:2]}-{number_part2[2:]}")
            date_parts = date_str.split("/")
            formatted_date = (f"{date_parts[2][-2:]}-{date_parts[1]}"
                              f"-{date_parts[0]}")
            new_table.append([mark, yN, formatted_number, formatted_date])
    return new_table

from pprint import pprint
pprint(main(data))
