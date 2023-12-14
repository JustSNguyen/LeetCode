from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_index = 0
        two_index = len(nums) - 1

        for i in range(len(nums)):
            while nums[i] != 1:
                if nums[i] == 0 and i < zero_index:
                    break
                if nums[i] == 2 and i > two_index:
                    break
                if nums[i] == 0:
                    nums[i], nums[zero_index] = nums[zero_index], nums[i]
                    zero_index += 1
                elif nums[i] == 2:
                    nums[i], nums[two_index] = nums[two_index], nums[i]
                    two_index -= 1

        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,0]
    result = sol.sortColors(nums)
    print(result)
