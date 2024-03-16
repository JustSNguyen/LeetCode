from typing import List 


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        disinct1 = set(nums1)
        result = set()
        for num in nums2:
            if num in disinct1:
                result.add(num)
        
        return list(result)