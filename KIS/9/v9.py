import re


def main(data_string):
    pattern = r'local\s+q\(([^)]+)\)\s+<-\s+@\'([^\']+)\';'
    data_dict = {}

    matches = re.findall(pattern, input_string)
    for match in matches:
        key = match[0]
        value = match[1]
        data_dict[key] = value

    return data_dict

# Пример использования
input_string = '{ <% let"arbi_991"enqued %> <% let "laties" ceabila_50 %><% let "anzain_269"maon %>}'
result = main(input_string)
print(result)
