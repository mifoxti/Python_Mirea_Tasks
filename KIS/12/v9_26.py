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
    offset = 3
    a1, offset = parse(buffer, offset, 'float')
    a2 = []
    for _ in range(2):
        a2_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_b(buffer, a2_offset)
        a2.append(val)
    a3, offset = parse_d(buffer, offset)
    a4, offset = parse(buffer, offset, 'double')
    a5_offset, offset = parse(buffer, offset, 'uint32')
    a5, _ = parse_e(buffer, a5_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint8')
    b2_offset, offset = parse(buffer, offset, 'uint32')
    b2, _ = parse_c(buffer, b2_offset)
    b3, offset = parse(buffer, offset, 'uint8')
    b4, offset = parse(buffer, offset, 'uint8')
    b5, offset = parse(buffer, offset, 'uint32')
    b6 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        b6.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3,
            'B4': b4, 'B5': b5, 'B6': b6}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'int64')
    c3, offset = parse(buffer, offset, 'int64')
    c4, offset = parse(buffer, offset, 'uint32')
    c5, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint64')
    d2, offset = parse(buffer, offset, 'float')
    d3 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint64')
        d3.append(val)
    d4, offset = parse(buffer, offset, 'double')
    d5, offset = parse(buffer, offset, 'uint64')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint8')
    e2, offset = parse(buffer, offset, 'int32')
    return {'E1': e1, 'E2': e2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'ITG\xbd\x11\xa5N\x00\x00\x00w\x00\x00\x00\xb2\r\xcb\xa0\xdb\xc9]\xca\x91>'
            b'vq\xe3\x82\xd9q\x96\xd2\xc2\xad%\xd1|\x0f\x9f\xd3\x1f\x80l\xef'
            b'\xcd\xf1\x17\xa5\x0e\xb0\x04?\xdcL\xf0X\xc8\xeb\xb8\x92F\x8d\x00\xadw\x9f<?'
            b"\xd3W[\xa8^K\x18\x00\x00\x00\xc3\xa7'\xf8)\x00\x00\x00\x02\x00\x00\x00O,"
            b'\xcc\x96K\x9c\xec\xc6\xde\xa8yl~"\x9c\xfc\xca\x00\x8dF\xcf\xbfYh\x00s'
            b'\xde\xdb\xdf\x8d\x00\x00\x00S\xdc\x88\xee\xad\x9c\xae\x00\x04\x00\x00\x00s'
            b'V\x1a\xdd\xd5\x00\x00\x00\x02\x00\x00\x00\x88E\xf4\xc2\xd2\xd1W\xa5\xb4'
            b'\xdc\xcc\x98dXv\xbby\x9d\xc7\x85\xb0\xbf\n5>x\xb0\xffR&,~\x00'
            b'\x00\x00\x8c\x1ft/\xe0\xaa\x18\x00\x06\x00\x00\x00\xac\xa3\x84*\xc0\xb0'))
