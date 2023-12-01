from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithemtic_subarray(l, r):
            subarray = []
            for i in range(l, r + 1):
                subarray.append(nums[i])

            if len(subarray) < 2:
                return False

            subarray = list(sorted((subarray)))
            prev_diff = subarray[1] - subarray[0]

            for i in range(2, len(subarray)):
                diff = subarray[i] - subarray[i - 1]
                if diff != prev_diff:
                    return False

            return True

        result = []
        for i in range(len(l)):
            result.append(is_arithemtic_subarray(l[i], r[i]))

        return result
