def main(data):
    seen = set()
    unique_rows = []
    for row in data:
        tuple_row = tuple(row)
        if tuple_row not in seen:
            seen.add(tuple_row)
            unique_rows.append(row)
    split_rows = []
    for row in unique_rows:
        email_date, name, number = row
        email, date = email_date.split(";")
        split_rows.append([email, date, name, number])
    transformed_rows = []
    for email, date, name, number in split_rows:
        date_parts = date.split('/')
        formatted_date = f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
        username = email.split('@')[0]
        name_parts = name.split()
        initials = f"{name_parts[0][0]}.{name_parts[1][0]}. {name_parts[2]}"
        percentage = f"{round(float(number) * 100)}%"
        transformed_rows.append([formatted_date, initials,
                                 username, percentage])
    transposed_table = list(map(list, zip(*transformed_rows)))
    return transposed_table


# Example usage:
input_data = [
    ["vosinan16@rambler.ru;03/02/08", "Герман Е. Вошинян", "0.198"],
    ["vosinan16@rambler.ru;03/02/08", "Герман Е. Вошинян", "0.198"],
    ["nikolaj10@yahoo.com;04/11/02", "Николай У. Метиди", "0.257"],
    ["vosinan16@rambler.ru;03/02/08", "Герман Е. Вошинян", "0.198"],
    ["fedor77@rambler.ru;01/06/16", "Федор Ц. Тавяк", "0.941"]
]

result = main(input_data)
for row in result:
    print(row)
