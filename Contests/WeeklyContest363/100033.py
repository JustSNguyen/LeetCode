from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        min_possible_number_of_alloys = 0
        max_possible_number_of_alloys = 10**9

        def possible(number_of_alloys):
            for machine in composition:
                required = [value * number_of_alloys for value in machine]
                need = [max(0, required[i] - stock[i]) for i in range(len(machine))]
                required_budget = 0
                for i in range(len(need)):
                    required_budget += need[i] * cost[i]

                if required_budget <= budget:
                    return True

            return False

        while max_possible_number_of_alloys - min_possible_number_of_alloys > 1:
            mid = (max_possible_number_of_alloys + min_possible_number_of_alloys) // 2

            if possible(mid):
                min_possible_number_of_alloys = mid
            else:
                max_possible_number_of_alloys = mid

        return min_possible_number_of_alloys

if __name__ == '__main__':
    sol = Solution()
    n = 3
    k = 2
    budget = 0
    composition = [[1,1,1],[1,1,10]]
    stock = [0,0,0]
    cost = [1,2,3]

    result = sol.maxNumberOfAlloys(n, k, budget, composition, stock, cost)
    print(result)