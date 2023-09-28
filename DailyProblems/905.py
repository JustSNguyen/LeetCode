from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_odd_index = len(nums) - 1
        i = 0

        while i < len(nums):
            num = nums[i]
            if num % 2 == 0:
                i += 1
                continue

            while nums[i] % 2 == 1 and last_odd_index > i:
                nums[i], nums[last_odd_index] = nums[last_odd_index], nums[i]
                last_odd_index -= 1

            i += 1

        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    result = sol.sortArrayByParity(nums)
    print(result)