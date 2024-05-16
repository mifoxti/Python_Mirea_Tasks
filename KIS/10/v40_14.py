data = [['873-999-4039', '873-999-4039', '5%', 'N'], ['044-360-0702', '044-360-0702', '35%', 'Y'], ['044-360-0702', '044-360-0702', '35%', 'Y'], ['044-360-0702', '044-360-0702', '35%', 'Y'], ['913-509-4945', '913-509-4945', '56%', 'Y'], ['761-475-0666', '761-475-0666', '69%', 'Y']]


def main(table):
    new_table = []
    unique_rows = set()
    slovar = {'Y': 'Да', 'N': 'Нет'}
    numbers = []
    marks = []
    yn = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number = string[0].split('-')
            formated_number = f"({number[0]}) {number[1]}-{number[2]}"
            mark = float(string[2].rstrip('%'))
            mark = "{:.3f}".format(mark / 100)
            yesorno = slovar[string[3]]
            numbers.append(formated_number)
            marks.append(mark)
            yn.append(yesorno)
    new_table.append(numbers)
    new_table.append(marks)
    new_table.append(yn)
    sorted_indices = sorted(range(len(new_table[0])),
                            key=lambda x: new_table[0][x])
    sorted_table = [[row[i] for i in sorted_indices] for row in new_table]
    return sorted_table


from pprint import pprint
pprint(main(data))