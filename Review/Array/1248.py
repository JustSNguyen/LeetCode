from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        max_odd_count = 0
        min_odd_count = 0
        j_max = 0
        j_min = 0
        result = 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                max_odd_count += 1
                min_odd_count += 1

            while max_odd_count > k:
                if nums[j_max] % 2 == 1:
                    max_odd_count -= 1

                j_max += 1

            while min_odd_count >= k:
                if nums[j_min] % 2 == 1:
                    min_odd_count -= 1
                    if min_odd_count < k:
                        min_odd_count = k
                        break

                j_min += 1

            if max_odd_count == k and min_odd_count == k and j_max <= i:
                result += (j_min - j_max + 1)

        return result


