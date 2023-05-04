from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        next_zero_index, next_two_index = 0, len(nums) - 1 
        index = 0 
        while index <= next_two_index:
            num = nums[index]
            if num == 0: 
                nums[index], nums[next_zero_index] = nums[next_zero_index], nums[index]
                next_zero_index += 1 
                index += 1 
            
            elif num == 1: 
                index += 1 
            
            else: 
                nums[index], nums[next_two_index] = nums[next_two_index], nums[index]
                next_two_index -= 1 
        

if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0, 1] 
    sol.sortColors(nums) 
    print(nums)