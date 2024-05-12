import re

string = '''<section> ( define[ "bier_312" ;"reusza_685" ; "tedi_624";"gequ"]->
@"inquis_187".), ( define ["arebe_871" ; "qumaor_832" ; "abiti" ;
"user_305" ] -> @"ceenbe". ), (define [ "diedin" ; "raeden" ;"isbiri"
; "edxe_15" ] -> @"isqu". ), (define ["edinin_295" ; "maonan" ] ->
@"inra_714". ), </section>'''

# Удаление символов новой строки
string = string.replace('\n', '')
string = string.replace(' ', '')
# string = string.replace(';', ' ')
print(string)
# Регулярное выражение для извлечения данных
# Используем регулярное выражение для поиска всех соответствий шаблону
matches = re.findall(r'\[\"(.*?)\"\]->@"(.*?)"\.', string)
# Формируем список кортежей из найденных соответствий
result = [(second, first.replace('"', '').split(';')) for first, second in matches]

print(result)
