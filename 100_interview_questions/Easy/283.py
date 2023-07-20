from typing import List 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cur_index = 0 

        for index, num in enumerate(nums): 
            if num == 0: continue 

            nums[cur_index], nums[index] = nums[index], nums[cur_index]

            cur_index += 1 
        
        