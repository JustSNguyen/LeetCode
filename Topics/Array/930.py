from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        at_most_goals = [goal, goal - 1]
        total = [0, 0]

        for i, at_most_goal in enumerate(at_most_goals):
            j1 = 0
            cur_sum = 0
            for j2 in range(len(nums)):
                cur_sum += nums[j2]
                
                while cur_sum > at_most_goal and j1 != j2:
                    cur_sum -= nums[j1]
                    j1 += 1 
                
                if cur_sum <= at_most_goal:
                    total[i] += (j2 - j1 + 1)
        
        return total[0] - total[1]