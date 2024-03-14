from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            required = -num
            lf = i + 1
            rg = len(nums) - 1

            while lf < rg:
                if nums[lf] + nums[rg] > required:
                    rg -= 1
                elif nums[lf] + nums[rg] < required:
                    lf += 1
                else:
                    result.append([num, nums[lf], nums[rg]])
                    while lf < rg and nums[lf + 1] == nums[lf]:
                        lf += 1

                    lf += 1

                    while lf < rg and nums[rg - 1] == nums[rg]:
                        rg -= 1

                    rg -= 1

        return result
