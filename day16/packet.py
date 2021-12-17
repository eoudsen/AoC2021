from PacketType import PacketType
from math import prod


class Packet:
    EVAL_HANDLERS = {
        PacketType.SUM: sum,
        PacketType.PRODUCT: prod,
        PacketType.MIN: min,
        PacketType.MAX: max,
        PacketType.GT: lambda args: args[0] > args[1],
        PacketType.LT: lambda args: args[0] < args[1],
        PacketType.EQ: lambda args: args[0] == args[1],
    }

    def __init__(self, header, value=None, subpackets=None):
        self.header = header
        self.value = value
        self.subpackets = subpackets or []

    def version_sum(self):
        return self.header.version_id + sum(subpacket.version_sum() for subpacket in self.subpackets)

    def eval(self):
        if self.header.type == PacketType.LITERAL:
            return self.value

        return self.EVAL_HANDLERS[self.header.type]([
            subpacket.eval() for subpacket in self.subpackets
        ])