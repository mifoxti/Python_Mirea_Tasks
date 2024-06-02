from struct import *


def parse(buffer, offset, type, order='>'):
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
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'uint32')
    a3, offset = parse(buffer, offset, 'uint8')
    a4, offset = parse(buffer, offset, 'double')
    a5, offset = parse(buffer, offset, 'int16')
    a6, offset = parse(buffer, offset, 'double')
    a7 = []
    for _ in range(2):
        a, offset = parse_c(buffer, offset)
        a7.append(a)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint64')
    b2 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b2 += val.decode()
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint16')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'double')
    c3_offset, offset = parse(buffer, offset, 'uint32')
    c3, _ = parse_d(buffer, c3_offset)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int8')
    d2, offset = parse(buffer, offset, 'float')
    d3, offset = parse(buffer, offset, 'float')
    d4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        d4.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'MUTQ\xdbG\x8c\x9ewP}\xc0\xbd\x00\x02\x00LD\xa3fhc?\xb8`\xdc\xc77\xaeppj'
            b'\xbf\xb6\xa2 \xb3\xfa\x9d`\xc9\xf2s\xaef\xc8?\xd57\xe9^A\xa3\x10\x00\x00'
            b'\x00R\xb8\xfb\xd0a\xd1\xf5?\xe2q\x07Q\x86\xe2\x1e\x00\x00\x00cix\xc0`'
            b'\xd6\xdbW=\x1a\xae\x91?p\xba\xb3\x00\x02\x00Nb\xd0\x13\x9a\x8d?E\x01-<\x9a3L'
            b'\x00\x02\x00_'))
