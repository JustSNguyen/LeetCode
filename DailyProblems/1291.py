from typing import List
import math

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def get_sequential_digits(start, length):
            result = 0
            for digit in range(start, start + length):
                result = result * 10 + digit

            return result

        min_length = math.trunc(math.log10(low)) + 1
        max_length = math.trunc(math.log10(high)) + 1
        result = []

        for length in range(min_length, max_length + 1):
            for start in range(1, 11 - length):
                num = get_sequential_digits(start, length)
                if num > high:
                    return result

                if low <= num <= high:
                    result.append(num)

        return result