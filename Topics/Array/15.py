from typing import List 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            j = i + 1
            k = N - 1 

            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if  cur_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    cur_j = nums[j]
                    while j < N and nums[j] == cur_j:
                        j += 1 
                    
                    cur_k = nums[k]
                    while k > i and nums[k] == cur_k:
                        k -= 1 
                elif cur_sum < 0:
                    j += 1 
                else:
                    k -= 1 
            
        return result 
        
