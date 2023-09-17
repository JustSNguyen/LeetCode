from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def get_number_of_one_bits(num):
            number_of_one_bits = 0

            while num > 0:
                bit = num % 2
                number_of_one_bits += bit
                num //= 2

            return number_of_one_bits

        sum_of_nums_with_exactly_k_one_bit = 0
        for index, num in enumerate(nums):
            number_of_one_bits = get_number_of_one_bits(index)
            if number_of_one_bits == k:
                sum_of_nums_with_exactly_k_one_bit += num

        return sum_of_nums_with_exactly_k_one_bit

if __name__ == '__main__':
    sol = Solution()
    nums = [4]
    k = 1
    result = sol.sumIndicesWithKSetBits(nums, k)
    print(result)