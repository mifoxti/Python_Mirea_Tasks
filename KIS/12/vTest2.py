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


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint64')
    d2, offset = parse(buffer, offset, 'double')
    d3, offset = parse(buffer, offset, 'int32')
    d4, offset = parse(buffer, offset, 'uint64')
    d5 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int8')
        d5.append(val)
    d6, offset = parse(buffer, offset, 'int32')
    d7 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'int8')
        d7.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6,
            'D7': d7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2 = buffer[offset:offset + 3].decode('ascii')
    offset += 3
    b3, offset = parse(buffer, offset, 'int32')

    b4 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        b4_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_c(buffer, b4_offset)
        b4.append(val)

    b5, offset = parse(buffer, offset, 'int64')
    b6 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'uint32')
        b6.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5, 'B6': b6}, offset


def parse_a(buffer, offset):
    offset = 4
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'double')
    a3, offset = parse(buffer, offset, 'uint16')
    a4, offset = parse(buffer, offset, 'int16')
    a5_offset, offset = parse(buffer, offset, 'uint32')
    a5, _ = parse_d(buffer, a5_offset)
    a6, offset = parse(buffer, offset, 'uint64')
    a7, offset = parse(buffer, offset, 'int64')
    a8, offset = parse(buffer, offset, 'uint16')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5, 'A6': a6,
            'A7': a7, 'A8': a8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


print(main(b'\xfbNWO\xb3Odiii&\xef&\x02\x00[\x00+\x13\xd2[0\xad\x7fky,\xc6z\xee[['
 b'\xa3\x18dj\xbb\x9b\xc0\xea?\x10\xb8\xef\xba_\x00\x00\x00i\x0b@\xcf\x1aSD'
 b"\xf4\xd8\xa0\x83\xc2V\xf9\x17\xce\x80'\x0e\x8b\xd0@;,\xe7?\x80\x1d\x19\xbf8"
 b't\xefN*J\xe5?\xb2\xf5\xa0>C\x00O\x00\x933\xe5\x93\n\xa0\n\xcb\xa8'
 b'\x95\xac\r\xcdz\xc6?\xd0\x06\xa6\x989z\x12c\xefm~8\xf7\xeb\x88\x07u'
 b'Q\xb8 \xed\xc7%\x03\xcd\xc0\xa4\x82\x97'))