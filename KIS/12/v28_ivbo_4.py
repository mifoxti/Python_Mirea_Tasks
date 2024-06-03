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
    offset = 4
    a1, offset = parse_b(buffer, offset)
    a2 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a2 += (val.decode())
    a3, offset = parse(buffer, offset, 'int64')
    a4, offset = parse(buffer, offset, 'float')
    a5, offset = parse_f(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2, offset = parse(buffer, offset, 'uint8')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int16')
    c2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse_d(buffer, adr_offset)
        c2.append(val)
    c3, offset = parse_e(buffer, offset)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint32')
    d2, offset = parse(buffer, offset, 'double')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int8')
    b2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        b2.append(val)
    return {'E1': e1, 'E2': b2}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'int8')
    f2, offset = parse(buffer, offset, 'uint8')
    f3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        f3.append(val)
    f4 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'uint64')
        f4.append(val)
    f5, offset = parse(buffer, offset, 'uint16')
    f6, offset = parse(buffer, offset, 'int32')
    f7, offset = parse(buffer, offset, 'int16')
    f8, offset = parse(buffer, offset, 'double')
    return {'F1': f1, 'F2': f2, 'F3': f3,
            'F4': f4, 'F5': f5, 'F6': f6,
            'F7': f7, 'F8': f8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'BMFNRH\x00\x00\x00\x03\x00NG\x00\x02\x00\x00\x00r\x99\x00\x00\x00\x02'
            b'\x00\x00\x00z\x8e\xccZ\xe1\x01\x17K\xed\xbf\x1c\x1ezY\x1a\x00\x03\x00|\xeaZ'
            b'\xcf21\xf69\x08\x15\xceUr\xce\xaf\x87\x0f\xd2\xbe2\rq\xde\x8d\x8f\xbf\xeb'
            b'-\xc3\xfc_\xa9H\\eK\xb8?\xe6\xf0\x98O:H\xf8\xab\xb5|\x05?\xebF\xa0\xba*'
            b'\t\xe09\xb7pZ\xbf\xb3\x12\x94\xf0\xfa\x7f\x00>\xf3\xf3\xb5?p#\x0bqx'
            b'\xbfW\xe3.?C\xf1\xe5?d\x1d\xb8'))
