import re


def main(input_string):
    input_string = input_string.replace('\n', '').replace(' ', '')
    pattern = r"store\s*'(\w+)'=:\s*(\w+)"
    matches = re.findall(pattern, input_string)
    result = [(value, name) for name, value in matches]
    return result


# Пример использования
input_string1 = "<data>{ store 'diridi_860'=:isti_728 }{ store'geri' =: esbein }{ store 'quesza_214' =:esiste } { store 'orlate' =:esates_906 } </data>"
input_string2 = "<data>{ store 'aorar'=: qudi }{store 'atte_846'=:usbequ } </data>"

parsed_result1 = main(input_string1)
parsed_result2 = main(input_string2)

print(parsed_result1)
print(parsed_result2)
