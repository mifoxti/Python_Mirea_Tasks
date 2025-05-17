def main(table):
    new_table = []
    unique_rows = set()
    nums = []
    marks = []
    dates = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            y, m, d = string[2].split('-')
            formated_date = f"{d}-{m}-{y}"
            phone_number, mark = string[0].split('#')

            formatted_number = (
                f"{phone_number[:2]} {phone_number[2:5]} "
                f"{phone_number[5:8]}-{phone_number[8:10]}-"
                f"{phone_number[10:]}"
            )
            formated_mark = f"{float(mark):.2f}"

            nums.append(formatted_number)
            marks.append(formated_mark)
            dates.append(formated_date)

    new_table.append(nums)
    new_table.append(dates)
    new_table.append(marks)
    return new_table


data = [['+77243993456#0.1', None, '27-01-00', '27-01-00'], ['+72870463230#0.4', None, '11-02-04', '11-02-04'],
        ['+72864265946#0.5', None, '01-12-99', '01-12-99'], ['+70311474225#0.5', None, '01-06-01', '01-06-01']]
from pprint import pprint

pprint(main(data))
