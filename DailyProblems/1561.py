from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = list(sorted(piles, reverse=True))

        result = 0
        number_of_piles_taken = 0

        i = 0

        while number_of_piles_taken < len(piles):
            result += sorted_piles[i + 1]
            number_of_piles_taken += 3
            i += 2

        return result