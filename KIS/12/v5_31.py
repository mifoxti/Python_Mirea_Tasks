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
    a1, offset = parse(buffer, offset, 'int64')
    a2, offset = parse(buffer, offset, 'int32')
    a3 = []
    for _ in range(5):
        e, offset = parse_b(buffer, offset)  # Parse structure E
        a3.append(e)
    a4 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a4 += (val.decode())

    a5, offset = parse(buffer, offset, 'uint8')
    a6, offset = parse_c(buffer, offset)
    a7, offset = parse(buffer, offset, 'float')
    a8 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        a8.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5,
            'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int32')
    b2, offset = parse(buffer, offset, 'uint64')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2, offset = parse(buffer, offset, 'uint64')
    d3, offset = parse(buffer, offset, 'int64')
    d4 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'uint8')
        d4.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'9EETV-*N\xe1\xa9!\xf7h\x10\xa1\x92\xd0cyC7\xa5\xb1i\xcb3\x88\x1c'
            b'\x98\xe6\x19\xd3L\xda\x8e<\n\xe8NK\x00\xb0\x1b\xda\xe6f\x82\\,7-\xad'
            b"f\xfem\x8ez\xa8p\xf7\x94\x12\xe8SL\tao'\x1f\xd8z\xca\xc9(!\n\x02\x00y"
            b"\x00\xa9\x0c\x9e\x15J\xbf\x934\xa5\x84\x88l\x82p\x0b>\xad\x12'\xc6\x00\xd1p"
            b'\xa2\xc4\xf9e\xec"4\xd06^\xbf\x03\x00{\x00\x00\x00zb\x89\x18g\xdcu\xb9'))
