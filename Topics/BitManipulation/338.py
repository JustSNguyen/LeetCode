from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        if n == 1:
            return [0, 1]

        largest_power_of_two_so_far = 1
        result = [0 for _ in range(n + 1)]
        result[1] = 1
        for num in range(2, n + 1):
            if num == largest_power_of_two_so_far * 2:
                result[num] = 1
                largest_power_of_two_so_far *= 2
            else:
                other = num - largest_power_of_two_so_far
                result[num] = 1 + result[other]

        return result



