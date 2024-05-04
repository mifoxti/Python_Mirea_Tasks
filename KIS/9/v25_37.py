import re


def main(input_string):
    # Удаляем пробелы из строки
    input_string = input_string.replace(" ", "")
    # Удаляем символы новой строки из строки
    input_string = input_string.replace("\n", "")

    # Создаем регулярное выражение для извлечения данных
    pattern = r'vararray\((.*?)\)to@(.*?);'

    # Ищем все соответствия регулярному выражению в строке
    matches = re.findall(pattern, input_string)

    # Создаем словарь для хранения результатов
    result = {}

    # Обрабатываем каждое соответствие
    for match in matches:
        # Извлекаем имя переменной и данные
        var_name = match[1].strip("'")  # Удаляем кавычки из ключа
        data = match[0].split('""')
        data = [element.replace('"', '') for element in data]

        # Добавляем данные в словарь
        result[var_name] = data

    return result


# Пример использования
input_string = '| <% var array( "eserge_11" "inlece" "edma""biin") to @\'isinin_4\';%>,\n<% var array("tiat""lexe_335" "tecein_930" )to @\'rionus_608\'; %>, <%\nvar array("anerma""onla_335" "onarqu_985" "reri_30") to @\'ised_396\';\n%>, <% var array("dice_645" "mati") to @\'anedin\'; %>, |'
parsed_result = main(input_string)
print(parsed_result)
