from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        maximum_possible = 0

        for coin in sorted(coins):
            if coin > maximum_possible + 1:
                return maximum_possible + 1

            maximum_possible += coin

        return maximum_possible + 1
