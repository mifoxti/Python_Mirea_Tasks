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
    offset = 5
    a1 = ''
    for _ in range(5):
        val, offset = parse(buffer, offset, 'char')
        a1 += (val.decode())
    a2, offset = parse_b(buffer, offset)
    a3 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a3 += (val.decode())
    a4, offset = parse(buffer, offset, 'int16')
    a5 = []
    for _ in range(6):
        a, offset = parse_d(buffer, offset)
        a5.append(a)
    a6, offset = parse(buffer, offset, 'float')
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4, 'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2, offset = parse(buffer, offset, 'double')
    b3, offset = parse(buffer, offset, 'int32')
    b4, offset = parse(buffer, offset, 'uint8')
    b5, offset = parse(buffer, offset, 'float')
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2, offset = parse(buffer, offset, 'int32')
    c3, offset = parse(buffer, offset, 'int32')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'MLVU\xf6hrnor\xc1Lk)\xe5\x0fuI\xdf\xa8\x08\xff+\xdc\xdb\xdd\xbfg'
            b'\xa3\x91\xf8\x920\xf2\x13\xbe\x03\x00\x00\x00\\\x00\x00\x00\xf3\xa3\x04\x00'
            b'\x00\x00_\x00\x83\x04\x00\x00\x00c\x00e\x04\x00\x00\x00g\x00\t\x06'
            b'\x00\x00\x00k\x00\x1b\x04\x00\x00\x00q\x00\xcb\x06\x00\x00\x00u\x00\x95'
            b'\x10v\x91\xbcwal\xef(yx\xa8\xa9\x19>S\x1b\xc9}\xe5\xdc\xc7\xb5\x82u\xbcgm'
            b'9\x16\xa8A\x8d\xb0p'))
