from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        number_of_houses = len(nums)
        rob_dp_result = [ [-1 for _ in range(2)] for _ in range(number_of_houses)]

        def rob_dp(index, robbed_previous_house): 
            if index == len(nums):
                return 0 
            
            if rob_dp_result[index][robbed_previous_house] != -1:
                return rob_dp_result[index][robbed_previous_house]
            
            if robbed_previous_house:
                rob_dp_result[index][robbed_previous_house] = rob_dp(index + 1, False);

            else: 
                rob_dp_result[index][robbed_previous_house] = max(rob_dp(index + 1, False), rob_dp(index + 1, True) + nums[index])
            
            return rob_dp_result[index][robbed_previous_house]
        
        if number_of_houses == 1:
            return nums[0] 
        
        return max(rob_dp(1, False), rob_dp(1, True) + nums[0])
    
if __name__ == "__main__":
    sol = Solution()
    nums = [2]
    result = sol.rob(nums)
    print(result)

