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
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a1 += (val.decode())
    a2, offset = parse(buffer, offset, 'float')
    a3_offset, offset = parse(buffer, offset, 'uint16')
    a3, _ = parse_b(buffer, a3_offset)
    a4, offset = parse(buffer, offset, 'uint8')
    a5 = ''
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        a5 += (val.decode())
    a6, offset = parse(buffer, offset, 'float')
    a7_offset, offset = parse(buffer, offset, 'uint32')
    a7, _ = parse_e(buffer, a7_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint64')
    b2_offset, offset = parse(buffer, offset, 'uint16')
    b2, _ = parse_c(buffer, b2_offset)
    b3, offset = parse(buffer, offset, 'int32')
    b4 = []
    for _ in range(7):
        d_offset, offset = parse(buffer, offset, 'uint32')
        d, _ = parse_d(buffer, d_offset)
        b4.append(d)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2, offset = parse(buffer, offset, 'int16')
    c3, offset = parse(buffer, offset, 'uint64')
    c4, offset = parse(buffer, offset, 'int32')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint16')
    d2, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int16')
    e2, offset = parse(buffer, offset, 'int64')
    e3, offset = parse(buffer, offset, 'int64')
    e4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint64')
        e4.append(val)
    e5, offset = parse(buffer, offset, 'uint64')
    e6, offset = parse(buffer, offset, 'int64')
    e7, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'KLLF\x00\x00\x00\x02\x00\x1b>w\xc7\xcd\x00H\x01ry>\t\x8fy\x00\x00\x00\x92e'
            b"z\xbf\xeb\\\xf9\x80P\xfd4J\xb26N'n3\xbd\xcc\x06\xa7\xc11\xf3\xfa\xfe~/\xeb"
            b"\xf5\xb4\x98'\xd2/\x00\xa4\x16\x83\xcc\xc3E\x87\x9b\xc5\xea=\xb1P"
            b'\x18Y\x14\x1e\x00\x1d\xda\x93\x1d\t\x00\x00\x003\x00\x00\x006\x00\x00'
            b'\x009\x00\x00\x00<\x00\x00\x00?\x00\x00\x00B\x00\x00\x00E\xa3\x03'
            b"\xf6\xa2\xe0'\xf4\x088C\xb3\xdd\x02\x85K\x9e\x01Z\x8b\xfc\xc7@\x1fH\xd7\x11"
            b'\xf0GK\xd3\xc6@\xc1l\xbf\x8c\xe9\x99\xfdA\x96\xfa3Ug\xc0x\x01*5'
            b'\x00\x00\x00\x04\x00\x00\x00r\x8b\xf0\xf2-\xfd\xd0e\xe7\xccr=G\xe6\xcf\xdft'
            b'\xc4H'))
