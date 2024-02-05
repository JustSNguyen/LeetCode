from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lf = 0
        rg = len(nums) - 1

        while lf < rg:
            if nums[lf] < nums[rg]:
                break
            mid = (rg + lf) // 2
            if nums[mid] > nums[-1]:
                lf = mid + 1
            else:
                rg = mid

        return nums[lf]