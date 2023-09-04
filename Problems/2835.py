from math import ceil
from typing import DefaultDict, List

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1 

        count = DefaultDict(int)
        for num in nums:
            count[num] += 1 

        need = DefaultDict(int)
        cur_base = 0
        while target > 0:
            bit = target % 2 
            if bit == 1:
                need[2 ** cur_base] = 1
            
            cur_base += 1 
            target //= 2 
        
        min_operations = 0 
        value = 1 

        
        while value <= max(nums):
            count[value] += count[value // 2] // 2
            if count[value] >= need[value]:
                count[value] -= need[value]
            else:
                need[value] -= count[value]
                count[value] = 0 
                debt = need[value] 
                min_operations += ceil(debt / 2)

                need[value * 2] += ceil(debt / 2)

            value *= 2  
        
        return min_operations 


if __name__ == '__main__':
    sol = Solution()
    nums = [16,16,4]
    target = 3
    result = sol.minOperations(nums, target)
    print(result)
        