from pprint import pprint
from struct import *


# РАБОТАЕТ
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
    offset = 4
    a1 = ''
    for _ in range(8):
        val, offset = parse(buffer, offset, 'char')
        a1 += (val.decode())
    a2, offset = parse(buffer, offset, 'int16')
    a3, offset = parse_b(buffer, offset)
    a4, offset = parse(buffer, offset, 'uint16')
    a5, offset = parse(buffer, offset, 'double')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1 = []
    for _ in range(2):
        e, offset = parse_c(buffer, offset)
        b1.append(e)
    b2, offset = parse_d(buffer, offset)
    b3, offset = parse(buffer, offset, 'int32')
    b4, offset = parse_e(buffer, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int64')
    c2, offset = parse(buffer, offset, 'int8')
    c3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint64')
        c3.append(val)
    c4, offset = parse(buffer, offset, 'uint8')
    c5, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2, offset = parse(buffer, offset, 'int16')
    d3, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int64')
    e2, offset = parse(buffer, offset, 'uint16')
    e3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        e3.append(val)
    return {'E1': e1, 'E2': e2, 'E3': e3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'BELWiqixqtiv\x82\x19\x04y*ZXg;An\x00\x00\x00\x02\x00[\x86?+\x0b\x8amg'
            b'\xd4\xb6\xde{c\xe5D\x00\x00\x00\x02\x00k\xda\xbf\x19\xae\x84>\x1a'
            b'\xdc\x9c:\xb6o\xeaWf\x10\xae\r+\xc6\xf5\x94\xf7?\xda\x95\x00\x03\x00\x00\x00'
            b'{\x82y?\xbe9\xf5`\xcbT\xa0\xc5\xcb\x11l\x14\x8fS\x02\x7f8\xd8\xb6\xc7'
            b"\x19_'\xc3@\x82\x83\x94\x8a\xae\xcdO\xa77I\x8f\xcc\xcd:\x83\xdf\x1a"))
