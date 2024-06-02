import re


def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = ("{:.0f}%".format(float(string[1]) * 100))
            day, month, year = string[0].split('-')
            fdate = f"{year}.{month}.{day}"
            digits_only = re.sub(r'\D', '', string[4])
            formatted_number = digits_only[-10:]
            formatted_number = (f"{formatted_number[:3]} "
                                f"{formatted_number[3:6]}-"
                                f"{formatted_number[6:]}")
            new_table.append([fdate, mark, formatted_number])
    return new_table


data = [['28-03-99', '0.672', None, '+7(035)823-44-45', '+7(035)823-44-45'],
        ['17-02-00', '0.654', None, '+7(466)226-55-58', '+7(466)226-55-58'],
        ['26-05-04', '0.186', None, '+7(257)405-70-92', '+7(257)405-70-92']]

print(main(data))
