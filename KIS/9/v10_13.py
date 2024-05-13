import re


def main(input_string):
    result = {}
    string = input_string.replace('\n', '')
    string_parse = string.replace(' ', '')
    matches = re.findall(r'doloc"([^"]+)"*:=*([+-]?\d+)\.', string_parse)
    for match in matches:
        key = match[0]
        value = int(match[1])
        result[key] = value
    return result


# Пример использования:
input_string = '|do loc "dige":= 689. end, do loc"bima":= 4162. end,do loc "indied" := -6352. end,do loc"xeso":= 3287. end, |'
parsed_result = main(input_string)
print(parsed_result)

input_string = '| do loc "laanve" := 883. end,do loc "lemais_801" := -8721. end, do loc "ininve" := -458. end, do loc "aza" :=9546. end, |'
parsed_result = main(input_string)
print(parsed_result)
