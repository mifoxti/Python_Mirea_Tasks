import re


def main(input_shit):
    pipi = re.sub(r'[\s\[\]\(\)\{\}\.\,]', '', input_shit)
    pattern = r"dostore(\w+)#(-?\d+)od"
    matches = re.findall(pattern, pipi)

    booba = {}
    for shittie, number in matches:
        booba[shittie] = int(number)

    return booba


# Примеры использования
input_string1 = "[[ do store vezage_9 #-5569 od. do store ores_412 #-9482 od. do store geer_559 #5424 od. ]]"
input_string2 = "[[ do store aton_72#587 od. do store atti #4305 od. ]]"
input_string3 = "[[ do store xeedon_534 #8982 od. do store diqu_375 #-4495 od. do\nstore isza #2995 od. ]]"

print(main(input_string1))  # {'vezage_9': -5569, 'ores_412': -9482, 'geer_559': 5424}
print(main(input_string2))  # {'aton_72': 587, 'atti': 4305}
print(main(input_string3))  # {'xeedon_534': 8982, 'diqu_375': -4495, 'isza': 2995}
