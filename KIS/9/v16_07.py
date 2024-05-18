import re


def main(input_string):
    pattern = r"`(\w+)\s*->\s*(\w+)\."
    matches = re.findall(pattern, input_string)
    result = [(value, key) for key, value in matches]
    return result


# Примеры использования
input_string1 = "begin[[ `veaerla_775 ->bexe. ]]; [[ `leor -> anaus_839. ]];[[ `xeatxe -> isma.]]; end"
input_string2 = "begin [[ `indi -> intian_49. ]]; [[ `laoris -> quared_249. ]];end"

print(main(input_string1))
print(main(input_string2))
