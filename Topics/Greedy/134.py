from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        SUM = sum(gas) - sum(cost)

        cur = 0
        start = 0
        N = len(gas)
        for i in range(N):
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                start = i + 1

        if start < N and SUM >= 0:
            return start

        return -1