import re


def main(strnorm):
    strnorm = strnorm.replace(' ', '').replace('\n', '')
    pattern = r"var#(-?\d+)\s*==>\s*(\w+)"
    matches = re.findall(pattern, strnorm)

    boobs = {}
    for number, name in matches:
        boobs[name] = int(number)

    return boobs


# Примеры использования
input_string1 = "<sect> << var #-2216 ==>rien>>. << var #-1157 ==>beriis_118 >>. <<var #-7894 ==> dimaar_258 >>. </sect>"
input_string2 = "<sect> <<var #-8789==>xege_227>>. << var #-3545 ==> geri >>. <<var #-8341==> mais >>. << var #-6877 ==>onri_972 >>. </sect>"
input_string3 = "<sect><< var#7642 ==>maza_893>>. << var#-9419 ==> enbiti >>. </sect>"

print(main(input_string1))  # {'rien': -2216, 'beriis_118': -1157, 'dimaar_258': -7894}
print(main(input_string2))  # {'xege_227': -8789, 'geri': -3545, 'mais': -8341, 'onri_972': -6877}
print(main(input_string3))  # {'maza_893': 7642, 'enbiti': -9419}
