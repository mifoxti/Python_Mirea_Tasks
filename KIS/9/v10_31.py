import re


def main(input_string):
    string = input_string.replace('\n', '')
    string = string.replace(' ', '')
    matches = re.findall(r'\[\"(.*?)\"\]->@"(.*?)"\.', string)
    result = []
    for first, second in matches:
        items = first.replace('"', '').split(';')
        if items:
            result.append((second, items))
    return result


from pprint import pprint

# Пример использования
input_string1 = '<section> (define [ "rimadi"; "zaus" ;"raonma_498"] -> @"geceon_921".), ( define ["anbe" ; "inreon" ]->@"alare". ),</section>'
pprint(main(input_string1))

input_string2 = '<section> ( define[ "bier_312" ;"reusza_685" ; "tedi_624";"gequ"]-> @"inquis_187".), ( define ["arebe_871" ; "qumaor_832" ; "abiti" ; "user_305" ] -> @"ceenbe". ), (define [ "diedin" ; "raeden" ;"isbiri" ; "edxe_15" ] -> @"isqu". ), (define ["edinin_295" ; "maonan" ] -> @"inra_714". ), </section>'
pprint(main(input_string2))

input_string3 = '<section> (define [ "rimadi"; "zaus" ;"raonma_498"] -> @"geceon_921".\n), ( define ["anbe" ; "inreon" ]->@"alare". ),</section>'
pprint(main(input_string3))
