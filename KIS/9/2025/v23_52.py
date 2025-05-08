import re


def main(text):
    result = []
    sect_blocks = re.findall(r'<sect>(.*?)</sect>', text, re.DOTALL)

    for block in sect_blocks:
        items = re.findall(r'q\((.*?)\)', block)
        destination = re.search(r'to\s+`(\w+)', block)
        if destination:
            result.append((destination.group(1), items))
    return result


input1 = '''<section> <sect> loc list( q(lete_13) q(tite_257) ) to `beente
</sect>,<sect> loc list( q(esen_747) q(geza)q(getied) q(anor) ) to
`tizama_260</sect>, <sect> loc list( q(onte) q(orce) q(zaesqu_623) )
to `cezadi</sect>, <sect> loc list( q(begeti_98) q(raleor_823))to
`zaor_178 </sect>,</section>'''

input2 = '''<section> <sect> loc list( q(cemare_932) q(orbi) ) to `reonle_23
</sect>, <sect> loc list( q(anatce)q(lezadi_634) )to `esbeis</sect>,
<sect> loc list( q(rixe)q(riuson) q(ratete) q(veonso) ) to `ered
</sect>, </section>'''

from pprint import pprint

pprint(main(input1))
pprint(main(input2))
