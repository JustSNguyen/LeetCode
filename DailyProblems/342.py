import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def is_integer(number: float) -> bool:
            return int(number) == number

        if n <= 0:
            return False

        sqrt_n = math.sqrt(n)
        if not is_integer(sqrt_n):
            return False

        log2_sqrt_n = math.log2(sqrt_n)
        return is_integer(log2_sqrt_n)

