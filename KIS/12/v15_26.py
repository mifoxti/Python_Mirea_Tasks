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
    a1, offset = parse(buffer, offset, 'double')
    a2, offset = parse(buffer, offset, 'int8')
    a3, offset = parse(buffer, offset, 'int32')
    a4, offset = parse(buffer, offset, 'uint8')
    a5, offset = parse_b(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint32')
    b2, offset = parse(buffer, offset, 'uint8')
    b3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        b3.append(val)
    b4, offset = parse(buffer, offset, 'int32')
    b5, offset = parse(buffer, offset, 'uint8')
    b6, offset = parse(buffer, offset, 'uint8')
    b7 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_d(buffer, adr_offset)
        b7.append(val)
    b8, offset = parse(buffer, offset, 'int16')
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5, 'B6': b6, 'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2, offset = parse(buffer, offset, 'int8')
    c3, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2, offset = parse(buffer, offset, 'int16')
    d3 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'int8')
        d3.append(val)
    d4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        d4.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'HEIZ\x1e"\x8fs\x89\xc7\xc9\xe0\xbfZ\xf2\xa0\xcd\x00U\x18\xb4\x1d\xcc\x9b'
            b'\x06\x00,\x00\x00\x00\xd5\xfe\xee\xc4\xf6\xd6\x02\x00V\x00\x00\x00\x87\xe6'
            b'\xb1\x83.\xaaP\xb90&\x80O\xe0Eu\x0f\xea\x98Z\xe1\xa1\xeb\x8a\xdbbz'
            b'\x1d\xcdN\x83\x81\xe8\xe7.\xf1l^\xf1ST\xf6\xc4&b\xff\\K\xbdY\x87fud\x15'
            b'4\x94\x05\x00D\x00\xec)y?Q\xa2j\x86c_c\xfa\x04\x00N\x00'))
