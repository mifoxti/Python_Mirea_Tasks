from pprint import pprint
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
    a1, offset = parse(buffer, offset, 'uint32')
    a2 = []
    for _ in range(7):
        a2_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_b(buffer, a2_offset)
        a2.append(val)
    a3, offset = parse(buffer, offset, 'int64')
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_c(buffer, a4_offset)
    a5, offset = parse(buffer, offset, 'uint64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int64')
    b2, offset = parse(buffer, offset, 'uint8')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        c1 += (val.decode())
    c2, offset = parse(buffer, offset, 'int16')
    c3, offset = parse_d(buffer, offset)
    c4, offset = parse(buffer, offset, 'uint16')
    c5 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'float')
        c5.append(val)
    c6, offset = parse(buffer, offset, 'double')
    c7 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'int16')
        c7.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6, 'C7': c7}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint16')
    d2, offset = parse(buffer, offset, 'uint16')
    d3, offset = parse(buffer, offset, 'float')
    d4, offset = parse(buffer, offset, 'double')
    d5, offset = parse(buffer, offset, 'uint64')
    d6, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5, 'D6': d6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b"FDC\x15Q\x1c;'\x000\x009\x00B\x00K\x00T\x00]\x00\xe5\x08\x1f\x10fVs"
            b'\xf7m\x00Qt\x89g\x12\x0b\xc8\xc4\xd7\xecp$\xdb\xech\x07\xc6\xe2\x84\x93O'
            b',\xe9\xd1\xa0\xc4l\xbe\xab\x19\x81P\x00h$\xbf\x11\xf4\xb6=sA\xdc\xa7\x05'
            b'\xc6+\x94\x16\xb5\xcfV]0\x0bj\xde\xa5\xe7\xa6\x1d\xf6\x1b"\xc3{|\xa6\xe0'
            b"\xf2\x1cyvaebxj\x07\x00\x00\x00f\x00\xc8\xfc\x1a;\xec\x0cA.\xd6=<Q'"
            b'\xb8\xfb/\xe3\xbfa\xd1gl\xd6\xed\xa5\x8d<\xa9\xfc&q\xc4\x16\xa6\xab\xbdY'
            b'1\xc2\xbd`\xd5N\n\xfb\x07\xb9?\xf1z@\xc2'))
