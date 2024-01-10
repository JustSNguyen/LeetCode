from typing import List 

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros_need_to_change = 0 
        max_length = 0 
        
        N = len(nums)
        j = 0 

        for i in range(N):
            if nums[i] == 0:
                zeros_need_to_change += 1 
            
            while zeros_need_to_change > k and j != i:
                if nums[j] == 0:
                    zeros_need_to_change -= 1 
                
                j += 1 
            
            if zeros_need_to_change <= k:
                max_length = max(max_length, i - j + 1)
        
        return max_length