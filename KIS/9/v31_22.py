import re


def main(data):
    data = data.replace('\n', ' ').replace(' ', '')
    pattern = r'local#\(([^)]+)\)to(\w+);'
    matches = re.findall(pattern, data)
    result = []
    for match in matches:
        numbers = list(map(int, match[0].split(';')))
        result.append((match[1], numbers))
    return result


# Примеры использования
input_str1 = r'\begin\begin local #(317 ;3905 ; -5360 ; -9809 )to bearge;\end \begin local#( -9389;-1898) to adidi; \end \end'
input_str2 = r'\begin \begin local #( 8491 ; -7555) to soedra; \end\begin local#( -9605 ;-1781 ) to dierra;\end \begin local #( 6408 ; 3135 ;6140; 4226 ) to atanis_774; \end \end'

print(main(input_str1))
print(main(input_str2))
