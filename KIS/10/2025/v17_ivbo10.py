def main(table):
    new_table = []
    surname = []
    marks = []
    dates = []
    unique_rows = set()

    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            d, m, y = string[2].split('.')
            f_day = f"{y}/{m}/{d}"
            mark, name = string[1].split('|')
            mark_value = int(mark.replace('%', ''))
            mark = f"{(mark_value / 100):.2f}"
            f_name = f"{name.split(' ')[0]}"
            surname.append(f_name)
            marks.append(mark)
            dates.append(f_day)

    new_table.append(surname)
    new_table.append(marks)
    new_table.append(dates)

    return new_table


print(main([
    [None, "15%|Ласивий А.Р.", "14.02.2004"],
    [None, "34%|Велянц А.К.", "13.12.2003"]
]))
