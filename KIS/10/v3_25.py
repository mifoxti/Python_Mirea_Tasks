def main(table):
    new_table = []
    unique_rows = set()
    slon = {'N': '0', 'Y': '1'}
    numbers = []
    yesorno = []
    marks = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            mark = string[0].ljust(5, '0')
            number = string[1].split('#')[0].split(' ')[2]
            yon = slon[string[1].split('#')[1]]
            marks.append(mark)
            yesorno.append(yon)
            numbers.append(number)
    new_table.append(marks)
    new_table.append(yesorno)
    new_table.append(numbers)
    return new_table


data = [[None, '+7 592 069-0226', '+7 592 069-0226', None, 'да&02/07/04'], [None, None, None, None, None],
        [None, '+7 834 670-4260', '+7 834 670-4260', None, 'да&00/08/19'],
        [None, '+7 581 869-8605', '+7 581 869-8605', None, 'да&01/12/18'],
        [None, '+7 790 574-5908', '+7 790 574-5908', None, 'да&99/01/13']]

from pprint import pprint

pprint(main(data))
