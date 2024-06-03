def main(table):
    new_table = []
    unique_rows = set()
    marks = []
    dates = []
    numbers = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(int(string[0].rstrip('%')) / 100)
            date = string[1].replace('/', '-')
            number = string[2].replace(' ', '').replace('-', '')
            numbers.append(number)
            dates.append(date)
            marks.append(mark)
    new_table.append(marks)
    new_table.append(dates)
    new_table.append(numbers)
    return new_table
