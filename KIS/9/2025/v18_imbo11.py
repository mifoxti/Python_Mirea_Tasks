import re


def main(text):
    pattern = re.compile(
        r"\.begin\s+make\s+list\(\s*([^\)]"
        r"+?)\s*\)\s*to\s*q\(\s*([^)]+?)\s*\)\s*;\s*\.end;",
        re.DOTALL
    )

    result = []
    for match in pattern.finditer(text):
        items_str, name = match.groups()
        items = items_str.split()
        result.append((name, items))

    return result


text1 = "do .begin make list( tius_810 diri esuser letiis )to q(anbe); .end;.begin make list(enus eris)to q(tiza); .end; done"
print(main(text1))
# [('anbe', ['tius_810', 'diri', 'esuser', 'letiis']), ('tiza', ['enus', 'eris'])]

text2 = """do .begin make list( intive arisor_311 soed ) to q(beri); .end;
.begin make list(onbi queser_162 ) to q(zalais); .end; .begin make
list(aaen beus rean_459 ) to q(tibi);.end;done"""
print(main(text2))
# [('beri', ['intive', 'arisor_311', 'soed']), ('zalais', ['onbi', 'queser_162']), ('tibi', ['aaen', 'beus', 'rean_459'])]
