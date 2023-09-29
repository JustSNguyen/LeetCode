from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums_length = len(nums)

        if nums_length <= 2:
            return True

        should_be_larger = nums[1] > nums[0]
        should_be_smaller = nums[1] < nums[0]

        for i in range(2, nums_length):
            if (nums[i] < nums[i - 1]) and should_be_larger:
                return False

            if (nums[i] > nums[i - 1]) and should_be_smaller:
                return False

            if nums[i] > nums[i - 1]:
                should_be_larger = True

            if nums[i] < nums[i - 1]:
                should_be_smaller = True

        return True
