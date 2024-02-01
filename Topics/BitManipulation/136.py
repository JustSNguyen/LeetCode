from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def flip(num, i):
            mask = 1 << i
            result = num ^ mask
            return result

        def get_ith_bit(num, i):
            return (num >> i) & 1

        MAX = 30001
        min_num = MAX
        max_num = -MAX
        mask = 0
        for num in nums:
            i = num
            if i < 0:
                i += 2 * MAX

            mask = flip(mask, i)

            min_num = min(min_num, num)
            max_num = max(max_num, num)

        for i in range(min_num, max_num + 1):
            j = i
            if i < 0:
                j += 2 * MAX

            if get_ith_bit(mask, j) == 1:
                return i

