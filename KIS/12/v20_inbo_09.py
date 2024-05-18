from struct import *


# РАБОТАЕТ
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
    offset = 4
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'int16')
    a3, offset = parse(buffer, offset, 'double')
    a4 = []
    for _ in range(7):
        a2_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_g(buffer, a2_offset)
        a4.append(val)
    a5, offset = parse_h(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2, offset = parse(buffer, offset, 'int32')
    b3, offset = parse(buffer, offset, 'uint32')
    b4, offset = parse(buffer, offset, 'uint64')
    b5, offset = parse_e(buffer, offset)
    b6, offset = parse(buffer, offset, 'double')
    b7, offset = parse(buffer, offset, 'uint8')
    b8, offset = parse(buffer, offset, 'int16')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        c1 += (val.decode())
    c2, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2, offset = parse(buffer, offset, 'int32')
    d3, offset = parse(buffer, offset, 'uint16')
    d4, offset = parse(buffer, offset, 'float')
    d5, offset = parse(buffer, offset, 'int16')
    d6, offset = parse(buffer, offset, 'float')
    d7, offset = parse(buffer, offset, 'uint32')
    d8, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7, 'D8': d8}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint8')
    e2, offset = parse(buffer, offset, 'uint8')
    e3, offset = parse(buffer, offset, 'int32')
    e4, offset = parse(buffer, offset, 'uint16')
    e5, offset = parse_f(buffer, offset)
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4, 'E5': e5}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'uint16')
    f2, offset = parse(buffer, offset, 'int16')
    return {'F1': f1, 'F2': f2}, offset


def parse_g(buffer, offset):
    g1, offset = parse(buffer, offset, 'int32')
    g2, offset = parse(buffer, offset, 'uint8')
    return {'G1': g1, 'G2': g2}, offset


def parse_h(buffer, offset):
    h1_offset, offset = parse(buffer, offset, 'uint32')
    h1, _ = parse_i(buffer, h1_offset)
    h2, offset = parse(buffer, offset, 'uint8')
    h3_offset, offset = parse(buffer, offset, 'uint32')
    h3, _ = parse_j(buffer, h3_offset)
    return {'H1': h1, 'H2': h2, 'H3': h3}, offset


def parse_i(buffer, offset):
    i1, offset = parse(buffer, offset, 'uint8')
    i2 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint32')
        i2.append(val)
    i3, offset = parse(buffer, offset, 'int8')
    return {'I1': i1, 'I2': i2, 'I3': i3}, offset


def parse_j(buffer, offset):
    j1 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'int16')
        j1.append(val)
    j2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        j2.append(val)
    j3, offset = parse(buffer, offset, 'int32')
    return {'J1': j1, 'J2': j2, 'J3': j3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b"\xdaCXA\x02\x00z\x00\\\t\xba>O\xc29?'\x15\xa8\\,\xbflu\x8f\xc9\x81\xbd"
            b';\x16\xf7\x825]A\xbf\xabf<\xc5?\xfd\xf0\xbf\x8e\x15\xae|\xb4\xa5\xf3\x1d'
            b'\x04o\x83\xdc\xea\x19\x8c\x99j|i\xf6Bf\n\x90\xa4\r\xea\xbfbx!W\x1c\xc0\xb9{'
            b'\x82\xee\xae\x99\xbf|\x00\x00\x00\x81\x00\x00\x00\x86\x00\x00'
            b'\x00\x8b\x00\x00\x00\x90\x00\x00\x00\x95\x00\x00\x00\x9a\x00\x00'
            b'\x00\x9f\x00\x00\x00\xc0\xb5\x00\x00\x00hx\xea\xeb\xcd\xde\n\xeeV\xc4'
            b'\x94\x9d\xbf\x82\x9e\xf5\x07g\xbcKp\xaa2\x02C\r\xd4"o\xa9\xbcz\xb1:'
            b'\xe2\xe2\xa8\xa8\xcc\xdc\xbcyxP\x83v\x8a\x8d\x91\xa5(\xea\xbf\x06?>\x82Y'
            b'>&\xfd\x99\xd9\x02\x00\xad\x00\x00\x00!\xf0M\xc2'))
