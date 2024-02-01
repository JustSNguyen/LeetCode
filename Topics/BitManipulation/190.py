import math


class Solution:
    def reverseBits(self, n: int) -> int:
        # Some notes:
        # 0x: This is a hexadecimal number
        # f = 16 (decimal) = 1111, 0 = 0 (decimal) = 0000
        # (n & 0xff00ff00): We keep the first 8 bits of each half. For example, if we have 32 bits like this:
        # n = 10110000 11110101 01001111 00001111 => (after the operation) n = 10110000 00000000 01001111 00000000

        n = n >> 16 | n << 16
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2
        n = (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1

        return n


