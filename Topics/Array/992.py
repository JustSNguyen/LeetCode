from typing import List 
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        at_most_list = [k, k - 1]
        total = [0, 0]

        for i, at_most in enumerate(at_most_list):
            diff_nums = defaultdict(int)

            j1 = 0 
            for j2 in range(len(nums)):
                diff_nums[nums[j2]] += 1 

                while len(diff_nums) > at_most and j1 != j2:
                    diff_nums[nums[j1]] -= 1 
                    if diff_nums[nums[j1]] == 0:
                        del diff_nums[nums[j1]]
                    
                    j1 += 1 
                
                if len(diff_nums) <= at_most:
                    total[i] += (j2 - j1 + 1)
        
        return total[0] - total[1]
            