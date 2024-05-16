import re


def main(input_string):
    pattern = r"variable\s*#\s*(-?\d+)\s*->\s*'([^']+)';"
    matches = re.findall(pattern, input_string)
    result = [(name, int(number)) for number, name in matches]
    return result

# Примеры использования
input_string1 = "{{variable #6097 -> 'esanra';}}, {{ variable#397 -> 'vesoer';}},"
input_string2 = "{{ variable #1949 ->'bior_669'; }},{{ variable#-2734 ->'bies';}}, {{ variable #-2907 ->'onra_25'; }},"

print(main(input_string1))
print(main(input_string2))
