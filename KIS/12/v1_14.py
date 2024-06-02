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
    a1, offset = parse(buffer, offset, 'float')
    a2 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a2 += (val.decode())
    a3, offset = parse(buffer, offset, 'uint16')
    a4, offset = parse(buffer, offset, 'uint8')
    a5, offset = parse(buffer, offset, 'int64')
    a6, offset = parse(buffer, offset, 'uint64')
    a7, offset = parse_b(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        b1.append(val)
    b2, offset = parse(buffer, offset, 'int8')
    b3, offset = parse(buffer, offset, 'uint8')
    b4, offset = parse(buffer, offset, 'uint32')
    b5, offset = parse_d(buffer, offset)
    b6 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b6.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5, 'B6': b6}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint16')
    c2, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint32')
    d2 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'int16')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'uint32')
    d4, offset = parse(buffer, offset, 'int8')
    d5 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint32')
        d5.append(val)
    d6, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5, 'D6': d6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'yHOBR\xd9\xec\x15?\x02\x00S\x00\x0f\x83B\x8b=\x02`\xf2\xe2w\xa0'
            b'\xe8\xa3\x10\xa8bG+\xce\x03\x00\x00\x00U\x00\x00\x00\\\xe8A\x19'
            b'\xad\x16\xd1\x89\xd4\x9fu\xaf `\x8eI\xca\xddNK\xa2\x1f\x9c\\w\xb9\x06\x0c'
            b'\xb8{#\x03\x00a\x00\xa1F\xa2\xbe\x05\x00m\x00sv\xb1 \xab_\x00\xbb\xd2'
            b'\x8d\xd9\xb9\xcd[?J\xc1\x9c\xd4\xad\xd8r\x95H\xd2n2r\xac)/'))
