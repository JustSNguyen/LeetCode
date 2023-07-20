from typing import List 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0 
        cur_total_gas = 0 

        ans = 0 
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            cur_total_gas += gas[i] - cost[i] 
            if cur_total_gas < 0:
                ans = i + 1 
                cur_total_gas = 0 
        
        return ans if total_gas >= 0 else -1 