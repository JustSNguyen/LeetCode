from typing import List 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i, num in enumerate(nums):
            target = -num 

            if i >= 1 and nums[i] == nums[i - 1]:
                continue 

            j1 = i + 1 
            j2 = len(nums) - 1 

            while j1 < j2: 
                cur_sum = nums[j1] + nums[j2]
                if cur_sum == target:
                    result.append([num, nums[j1], nums[j2]])

                    while j1 + 1 < j2 and nums[j1 + 1] == nums[j1]:
                        j1 += 1 

                    while j2 - 1 > j1 and nums[j2 - 1] == nums[j2]:
                        j2 -= 1 
                    
                    j1 += 1 
                    j2 -= 1 

                if cur_sum < target:
                    j1 += 1 
                
                if cur_sum > target:
                    j2 -= 1 
            
        return result 

if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    result = sol.threeSum(nums)
    print(result)
        