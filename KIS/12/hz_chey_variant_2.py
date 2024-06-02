from struct import *


class Type:
    float = 'f'
    double = 'd'
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'


def parse(buffer, offset, type, order='>'):
    size = calcsize(order + type)
    value = unpack_from(order + type, buffer, offset)[0]
    return value, offset + size


def parse_d(buffer, offset):
    d1size, offset = parse(buffer, offset, Type.uint32)
    d1offs, offset = parse(buffer, offset, Type.uint16)
    d1 = []
    for _ in range(d1size):
        val, d1offs = parse(buffer, d1offs, Type.int32)
        d1.append(val)

    d2, offset = parse(buffer, offset, Type.int32)
    d3, offset = parse(buffer, offset, Type.int16)
    d4, offset = parse(buffer, offset, Type.uint8)

    d5size, offset = parse(buffer, offset, Type.uint16)
    d5offs, offset = parse(buffer, offset, Type.uint32)
    d5 = []
    for _ in range(d5size):
        val, d5offs = parse(buffer, d5offs, Type.uint16)
        d5.append(val)
    d6, offset = parse(buffer, offset, Type.int64)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, Type.int8)
    c2, offset = parse(buffer, offset, Type.float)
    c3, offset = parse(buffer, offset, Type.uint16)
    c4, offset = parse(buffer, offset, Type.float)
    c5, offset = parse(buffer, offset, Type.int32)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5}, offset


def parse_b(buffer, offset):
    b1 = []
    array_size, offset = parse(buffer, offset, Type.uint16)
    adr_offset, offset = parse(buffer, offset, Type.uint32)
    for _ in range(array_size):
        b1_offset, adr_offset = parse(buffer, adr_offset, Type.uint16)
        val, _ = parse_c(buffer, b1_offset)
        b1.append(val)

    b2size, offset = parse(buffer, offset, Type.uint16)
    b2offs, offset = parse(buffer, offset, Type.uint16)
    b2 = ""
    for _ in range(b2size):
        val, b2offs = parse(buffer, b2offs, Type.char)
        b2 += val.decode()

    b3, offset = parse(buffer, offset, Type.double)

    b4_offset, offset = parse(buffer, offset, Type.uint32)
    b4, _ = parse_d(buffer, b4_offset)

    b5, offset = parse(buffer, offset, Type.int16)
    b6, offset = parse(buffer, offset, Type.int32)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5, 'B6': b6}, offset


def parse_a(buffer, offset):
    a1, offset = parse(buffer, offset, Type.int64)
    a2_offset, offset = parse(buffer, offset, Type.uint16)
    a2, _ = parse_b(buffer, a2_offset)
    return {'A1': a1, 'A2': a2}, offset


def main(data):
    result, _ = parse_a(data, 5)
    return result


if __name__ == '__main__':
    from pprint import pprint
    pprint(main(b'\xfcKVUZ0\x95\xd0\x80~\n\xe8f\x00t]\xbe\xf2-<\xe5\x81?p\xf2J\xa9\xed'
               b'B\x96\xde\xbfs\xef\x96\xc9\x7f\xbf\x12\x1a\x05\x1d\xb0/\x88\xa0\xbd\xae'
               b'\xa5q\x85k?y\xdd\xd4_\xc0\xd9A\x00\x0f\x00\x1e\x00-mtt\x95\xbd\x8b\xf3GB\xf9'
               b'\xbcC\x8bn\xe9\x1e\xab3v\x998\x0c7\x00\x00\x00\x02\x00Ea\xa4(\xbf4'
               b'\x8e\xa3\x00\x06\x00\x00\x00M\x1a\xec \x8e\xb6#\xa6w\x00\x03\x00\x00'
               b'\x00<\x00\x03\x00B\xbfY\xd1.\xe8\xd1 \x00\x00\x00\x00Yi\rz\xc1\xe0\xdb'))
