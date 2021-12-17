from header import Header
from PacketType import PacketType
from packet import Packet


def shift(data, num_bits, binary=False):
    bits = data[:num_bits]
    return bits if binary else int(bits, 2), data[num_bits:]


def parse_header(data):
    version_id, data = shift(data, 3)
    type_id, data = shift(data, 3)
    header = Header()
    header.version_id = version_id
    header.type = PacketType(type_id)
    return header, data


def parse_literal(data):
    value = 0
    group_bit, data = shift(data, 1)

    while group_bit == 1:
        group, data = shift(data, 4)
        value = 16 * value + group
        group_bit, data = shift(data, 1)

    group, data = shift(data, 4)
    value = 16 * value + group
    return value, data


def parse_subpackets_by_length(data):
    total_length, data = shift(data, 15)
    subpacket_data, data = shift(data, total_length, binary=True)
    subpackets = []

    while subpacket_data:
        subpacket, subpacket_data = parse_packet(subpacket_data)
        subpackets.append(subpacket)

    return subpackets, data


def parse_subpackets_by_count(data):
    total_subpackets, data = shift(data, 11)
    subpackets = []

    for _ in range(total_subpackets):
        subpacket, data = parse_packet(data)
        subpackets.append(subpacket)

    return subpackets, data


def parse_packet(data):
    header, data = parse_header(data)

    if header.type == PacketType.LITERAL:
        value, data = parse_literal(data)
        return Packet(header, value=value), data

    length_type_id, data = shift(data, 1)

    if length_type_id == 0:
        subpackets, data = parse_subpackets_by_length(data)
    else:
        subpackets, data = parse_subpackets_by_count(data)

    return Packet(header, subpackets=subpackets), data


def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


def parse_transmission():
    transmission = hex_to_bin(open('input.txt').readline())
    packet, _ = parse_packet(transmission)
    return packet


def solve():
    transmission = parse_transmission()
    return transmission.version_sum()


def solve2():
    transmission = parse_transmission()
    return  transmission.eval()


if __name__ == '__main__':
    print(solve())
    print(solve2())
