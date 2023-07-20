from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        
        for num in nums1:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        
        result = []
        for num in nums2:
            if num in hashmap and hashmap[num] > 0:
                result.append(num)
                hashmap[num] -= 1 
        
        return result 