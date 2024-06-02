def main(table):
    new_table = []
    unique_rows = set()
    slon = {'нет': '0', 'да': '1'}
    numbers = []
    yesorno = []
    dates = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            number_formed = string[1][3::].replace(' ', '-')
            yn = slon[string[4].split('&')[0]]
            date = string[4].split('&')[1].replace('/', '.')
            numbers.append(number_formed)
            yesorno.append(yn)
            dates.append(date)
    new_table.append(numbers)
    new_table.append(yesorno)
    new_table.append(dates)
    return new_table


data = [[None, '+7 592 069-0226', '+7 592 069-0226', None, 'да&02/07/04'], [None, None, None, None, None],
        [None, '+7 834 670-4260', '+7 834 670-4260', None, 'да&00/08/19'],
        [None, '+7 581 869-8605', '+7 581 869-8605', None, 'да&01/12/18'],
        [None, '+7 790 574-5908', '+7 790 574-5908', None, 'да&99/01/13']]

from pprint import pprint

pprint(main(data))
