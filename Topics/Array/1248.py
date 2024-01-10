from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_number_count_1 = 0
        odd_number_count_2 = 0
        i2 = 0
        i1 = 0
        result = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                odd_number_count_1 += 1
                odd_number_count_2 += 1

            while odd_number_count_1 > k:
                if nums[i1] % 2 == 1:
                    odd_number_count_1 -= 1

                i1 += 1

            while odd_number_count_2 >= k:
                if nums[i2] % 2 == 1:
                    odd_number_count_2 -= 1
                    if odd_number_count_2 < k:
                        odd_number_count_2 += 1
                        break

                i2 += 1

            if odd_number_count_1 == k and odd_number_count_2 == k:
                result += i2 - i1 + 1

        return result