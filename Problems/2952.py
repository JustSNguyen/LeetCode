from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        max_possible = 0
        addition = 0
        for coin in sorted(coins):
            if max_possible >= target:
                return addition

            if coin > max_possible + 1:
                addition += 1
                max_possible += max_possible + 1
            else:
                max_possible += coin

        return addition

if __name__ == '__main__':
    sol = Solution()
    coins = [1,4,10,5,7,19]
    target = 19
    result = sol.minimumAddedCoins(coins, target)
    print(result)