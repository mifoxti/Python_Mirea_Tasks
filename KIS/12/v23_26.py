from struct import *


def parse(buffer, offset, type, order='<'):
    pattern = {
        'float': 'f',
        'double': 'd',
        'char': 'c',
        'int8': 'b',
        'uint8': 'B',
        'int16': 'h',
        'uint16': 'H',
        'int32': 'i',
        'uint32': 'I',
        'int64': 'q',
        'uint64': 'Q'
    }[type]
    size = calcsize(order + pattern)
    value = unpack_from(order + pattern, buffer, offset)[0]
    return value, offset + size


def parse_a(buffer, offset):
    offset = 3
    a1, offset = parse_b(buffer, offset)
    a2_offset, offset = parse(buffer, offset, 'uint16')
    a2, _ = parse_c(buffer, a2_offset)
    return {'A1': a1, 'A2': a2}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int64')
    b2, offset = parse(buffer, offset, 'int32')
    b3, offset = parse(buffer, offset, 'int64')
    return {'B1': b1, 'B2': b2,
            'B3': b3}, offset


def parse_c(buffer, offset):
    c1 = ''
    for _ in range(8):
        val, offset = parse(buffer, offset, 'char')
        c1 += (val.decode())
    c2 = []
    for _ in range(2):
        b3_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_d(buffer, b3_offset)
        c2.append(val)
    c3, offset = parse(buffer, offset, 'uint32')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        d2.append(val)
    d3 = []
    for _ in range(7):
        a, offset = parse(buffer, offset, 'float')
        d3.append(a)
    d4 = []
    for _ in range(4):
        a, offset = parse(buffer, offset, 'uint16')
        d4.append(a)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'EKIf_4\xa78\xec\x8d\xaeUg,\xf4y\t6m\x0cE\xa4\\\x87\x00\xa1\x80\xd8J)\x00O'
            b'\xbf\x02\x00\x00\x00\x19\x00\x00\x00&\x96\t?\x88\xd7\x81\xbe\xed\x99\x92'
            b'\xbe\xa3\r\x18\xbf55\xaa=\xa0\x00\xee>\xda0>?\xdc;Vct\xff\xb4\xff$6\xf7'
            b'\x81\x16tW\xcd\x94\xc6\xc4\x91d?\x05\x00\x00\x00M\x00\x00\x00}BS\xbfq'
            b'\xf4\x02?,\xde\x1a\xbfL\xc0L\xbe\x15\x7f\xc8=y\x85\xdb>L8$\xbe4'
            b'\xff\xf4\xee\x83t\xa0Xyncsfkzp\x1d\x00\x00\x00W\x00\x00\x00I\xab\xb43'))
