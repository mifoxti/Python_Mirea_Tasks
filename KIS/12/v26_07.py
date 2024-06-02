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
    offset = 5
    a1, offset = parse(buffer, offset, 'uint32')
    a2, offset = parse(buffer, offset, 'int16')
    a3_offset, offset = parse(buffer, offset, 'uint16')
    a3, _ = parse_b(buffer, a3_offset)
    a4, offset = parse_d(buffer, offset)
    a5, offset = parse(buffer, offset, 'float')
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4, 'A5': a5}, offset


def array_gen(buffer, offset, siz, ofs, type):
    mass = []
    array_siz, offset = parse(buffer, offset, siz)
    adr_offset, offset = parse(buffer, offset, ofs)
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, type)
        mass.append(val)
    return mass, offset


def parse_b(buffer, offset):
    b1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        b1.append(val)
    b2, offset = array_gen(buffer, offset, 'uint16', 'uint32', 'float')
    b3, offset = array_gen(buffer, offset, 'uint16', 'uint16', 'float')
    b4, offset = array_gen(buffer, offset, 'uint32', 'uint32', 'float')
    b5, offset = parse(buffer, offset, 'uint8')
    return {'B1': b1, 'B2': b2,
            'B3': b3, 'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'WGGK\xc2\xc69\x8e\xf2 \xd9B\x00{Y_ t\x07\xbe3!1\xa8>\xe7\xab\xa1'
        b'\x9c\xbe\xd6\xff\xb9<\xa2\xf9B>\x92mY\xbf\xd5\x130>\xd63\xa8\xbe6\x00M?m\xe8'
        b'y\xbe+\xf1?\xbf\x80RP>\x02\x00\x14\x00\x03\x00\x1e\x00\x00\x00\x04\x00*\x00'
        b'\x02\x00\x00\x00:\x00\x00\x00\xb0')

from pprint import pprint

pprint(main(data))
