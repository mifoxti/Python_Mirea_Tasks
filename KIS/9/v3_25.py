import re


def parse_string(pizdozavr):
    pizdozavr = pizdozavr.replace('\n', '')
    pizdozavr = pizdozavr.replace(' ', '')
    pattern = r"\{([^{}]+?)\}\s*=\s*:@'([^']*)'"
    matches = re.findall(pattern, pizdozavr)
    result = {}
    for match in matches:
        values = [value.strip()
                  for value in match[0].split(",")
                  if value.strip()]
        result[match[1]] = values
    return result


# Пример использования функции с вашими данными
input_string = "<%(data {aat_493,argera_632 , orxeer } =:@'geraen_383'; );(data { esed, receon} =: @'orra_119';); ( data { onesus , abeaon_4 } =:@'esreis_157'; ); %>"
print(parse_string(input_string))

input_string = "<% ( data {bila , inin , rige , inla_407} =: @'veinin';); ( data { enle , ener_489 , lebeon} =: @'erma'; ); %>"
print(parse_string(input_string))
