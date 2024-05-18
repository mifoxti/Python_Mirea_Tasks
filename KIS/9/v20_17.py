import re


def main(input_string):
    pattern = r"local\s+(\w+)\s*<\|\s*#(-?\d+)"
    matches = re.findall(pattern, input_string)
    result = [(name, int(value)) for name, value in matches]
    return result


# Примеры использования
input_string1 = "[ {local rege_190 <|#-1925}, { local inen_4 <|#-7111 }, ]"
input_string2 = "[{ local rion_721<| #5350 }, { local erer_825 <| #-3730 }, { local rieres_641 <| #-5484 }, { local enxe <|#1036}, ]"

print(main(input_string1))
print(main(input_string2))
