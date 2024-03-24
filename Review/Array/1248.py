from typing import List 

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        first_seen = dict()
        first_seen[0] = -1 

        last_seen = dict()
        last_seen[0] = -1 

        result = 0 
        prefix = 0 

        for i, num in enumerate(nums):
            if num % 2 == 1:
                prefix += 1 

            other = prefix - k 
            if other in first_seen:
                result += last_seen[other] - first_seen[other] + 1 
                
            if prefix not in first_seen:
                first_seen[prefix] = i 

            last_seen[prefix] = i 

        return result             