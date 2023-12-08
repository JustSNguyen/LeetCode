from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        max_possible = 0
        addition = 0
        sorted_coins = sorted(coins)
        coin_index = 0

        while max_possible < target:
            if coin_index >= len(coins) or sorted_coins[coin_index] > max_possible + 1:
                addition += 1
                max_possible += max_possible + 1
            else:
                max_possible += sorted_coins[coin_index]
                coin_index += 1

        return addition

if __name__ == '__main__':
    sol = Solution()
    coins = [1,4,10,5,7,19]
    target = 19
    result = sol.minimumAddedCoins(coins, target)
    print(result)