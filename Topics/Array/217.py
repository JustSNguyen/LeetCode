class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev = None 
        for num in sorted(nums):
            if num == prev:
                return True 

            prev = num 

        return False         