class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1 
        i = 0 
        cur_sum = 0 
        for j in range(len(nums)):
            cur_sum += nums[j]

            while cur_sum >= target and i != j:
                cur_sum -= nums[i]
                if cur_sum < target: 
                    cur_sum += nums[i]
                    break 
                i += 1 
            
            if cur_sum >= target:
                min_length = min(min_length, j - i + 1)
        
        if min_length == len(nums) + 1:
            return 0
        
        return min_length