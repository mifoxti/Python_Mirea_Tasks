import re


def parse_string(input_string):
    # Паттерн для поиска пар "ключ => значение"
    pattern = r"local\s+q\((\w+)\)\s*<-\s*@'([^']+)';"

    # Ищем все соответствия паттерну во входной строке
    matches = re.findall(pattern, input_string)

    # Создаём словарь, используя найденные соответствия
    result = {key: value for key, value in matches}

    return result


# Примеры использования функции
input_string1 = "<:{{ local q(usleed) <- @'latiin'; }},{{local q(raen) <- @'geaedon_458'; }},{{ local q(eddies_987) <- @'arbele_158';}}, {{local q(labera_340) <- @'oris_136'; }},:>"
input_string2 = "<: {{ local q(esar) <- @'isce';}}, {{local q(georza) <- @'tirabi'; }},{{ local q(ceardi) <- @'geatri'; }}, {{local q(anlear_543)<- @'tearle';}},:>"

print(parse_string(input_string1))
print(parse_string(input_string2))
