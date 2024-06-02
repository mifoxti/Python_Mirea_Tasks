import re


def main(input_string):
    cleaned_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r'let([\w_]+)<==\"([^\"]+)\";'
    matches = re.findall(pattern, cleaned_string)
    result = [(match[0], match[1]) for match in matches]
    return result


# Пример использования
input_string1 = '(( begin let biusti_884 <== "bera";end begin let tiorle_82 <== "atdila_309";end ))'
input_string2 = '(( begin let xeardi<== "eren"; end begin let tien_275 <== "orla"; end))'

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
