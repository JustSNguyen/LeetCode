from typing import List 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen_index = dict()

        first_seen_index[0] = -1 

        prefix_sum = 0 
        max_length = 0
        for i, num in enumerate(nums):
            prefix_sum += (num if num == 1 else -1) 
            if prefix_sum not in first_seen_index:
                first_seen_index[prefix_sum] = i 
            else:
                j = first_seen_index[prefix_sum]
                max_length = max(max_length, i - j)
        
        return max_length