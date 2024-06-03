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
    a1 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_b(buffer, a3_offset)
        a1.append(val)
    a2 = []
    for _ in range(5):
        a, offset = parse_c(buffer, offset)
        a2.append(a)
    a3 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'float')
        a3.append(val)
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_d(buffer, a4_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1 = ''
    for _ in range(3):
        val, offset = parse(buffer, offset, 'char')
        b1 += (val.decode())
    b2, offset = parse(buffer, offset, 'uint16')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int32')
    c2, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'double')
    d2, offset = parse(buffer, offset, 'float')
    d3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        d3.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'JPWOo\x02\x00\x00\x00G\x00\x00\x00wC\xb0\xb0\x08DEg[\x8f\x88\xfb\x05\x8aL'
            b'\x9b\xe1\xffz\xb1\xed\xe2a\xe8.>w;-\xbf\x8191\xbfy\xdc:\xbeH\x95\x0c?\x9b'
            b'p\x0e\xbfQ\x00ymdW\x96tfbaq=\x00\x00\x00B\x00\x00\x00\xb5\xcbT>\xe8'
            b'\xf1\x90\x9c\xdf?\xbaC;\xbf\x02\x00\x00\x00O\x00'))
