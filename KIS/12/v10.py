from struct import *

# НЕ РАБОТАЕТ
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
    a1_offset, offset = parse(buffer, offset, 'uint16')
    a1, _ = parse_b(buffer, a1_offset)
    a2 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a2_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_d(buffer, a2_offset)
        a2.append(val)
    a3, offset = parse(buffer, offset, 'uint8')
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'char', '>3')
    b2, offset = parse(buffer, offset, 'int32')
    b3, offset = parse(buffer, offset, 'int64')
    b4, offset = parse(buffer, offset, 'int16')
    b5, offset = parse(buffer, offset, 'int16')
    b6, offset = parse(buffer, offset, 'int32')
    b7, offset = parse(buffer, offset, 'uint16')
    b8_offset, offset = parse(buffer, offset, 'uint32')
    b8, _ = parse_c(buffer, b8_offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'int32')
    c3, offset = parse(buffer, offset, 'int8')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2, offset = parse(buffer, offset, 'float', '>8')
    d3, offset = parse(buffer, offset, 'uint16', '>8')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


print(main((b'\xedWKW\x00\x00\x00\x1c\x00\x02\x00\x9dU\xe51\xd5\x1bp!\x00\x03\x00\r\x92'
            b"%'\x7f\xf1dki\xce\x86\x92\x16H\x84\x8d\x10|\x94T\x14\xc0\x97\xa3\x91\xa3"
            b'\xc7\xd6\x00\xfd\xa9\x00\x00\x00\x13\xe1,\xbfB\xcbv\xbf0\x81\xfe?2\xd1\xb9?'
            b'D\xa8\x08=\xe9p0\xbd\xf9v\x1d\xbd\xe8\xe8\xb7\xbe\xd42\xa3<\xb8\x0c\xa1\x90'
            b'w\x84\x9c\xd5\x14\xe8\xa6\xdb\x12\x98\xc7\xecN\xbf\x0e7X\xbd\xc9\xe6'
            b'V?\x16\x99\xf4>(\xef\xf9>\xdcrm\xbf1!A?)\xa8E?\rp\x95\xc0\x9c\xe5\xf4 <\xc5'
            b"\x85\x87'^\xd6\xe1\xec\x931\x009\x00k")))
