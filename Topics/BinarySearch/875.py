from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        N = len(piles)
        def is_possible(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)

            return total <= h

        lf = 0
        rg = max(piles)

        while rg - lf > 1:
            mid = (rg + lf) // 2
            if is_possible(mid):
                rg = mid
            else:
                lf = mid

        return rg

