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
    offset = 3
    a1 = ''
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        a1 += (val.decode())
    a2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_b(buffer, adr_offset)
        a2.append(val)
    a3_offset, offset = parse(buffer, offset, 'uint16')
    a3, _ = parse_c(buffer, a3_offset)
    a4, offset = parse(buffer, offset, 'uint8')
    a5, offset = parse(buffer, offset, 'double')
    a6_offset, offset = parse(buffer, offset, 'uint16')
    a6, _ = parse_d(buffer, a6_offset)
    a7 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        a7.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b2.append(val)
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'uint32')
    c3, offset = parse(buffer, offset, 'uint32')
    c4, offset = parse(buffer, offset, 'uint8')
    c5, offset = parse(buffer, offset, 'uint16')
    c6, offset = parse(buffer, offset, 'double')
    c7, offset = parse(buffer, offset, 'uint16')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6, 'C7': c7}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint64')
    d2, offset = parse(buffer, offset, 'uint64')
    d3, offset = parse(buffer, offset, 'uint64')
    d4, offset = parse(buffer, offset, 'uint64')
    d5, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'DLWvy\x02\x00\x00\x00$\x00\x00\x008\x00U\xfa \xbd\x1d\x03\xd4\xe7?'
            b'S\x00\x05\x00\x00\x00t\x00\xd2ls\xc5\xaa\x0b\x02\x00 \x00m/\x02\x00"\x00'
            b"\xca\xe4n=\x0e\xae\xc7>\x02\x000\x00\x00\x00JdU\x07 '\x0f\xfcj\xef"
            b'\xd9\xc8\x85\xa5\xed\xa18\xed?\xea\x17\x7f<^\xe0\xa2K\x9a\xedt\x8cz\xcd\xd1'
            b'e\xd6C=\xa9\x82\xb5b\x15\t\xaf\n,\x19\xfe)\xb1\\\x05\xdb\xce\x8f\xe3\xdc{'))
