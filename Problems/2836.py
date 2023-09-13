import math
from typing import List
from functools import lru_cache

class Solution:
    def getMaxFunctionValue(self, next_receiver: List[int], k: int) -> int:
        log_2_k = math.floor(math.log(k, 2))
        number_of_passers = len(next_receiver)
        receiver = [[0 for _ in range(log_2_k + 1)] for _ in range(number_of_passers)]
        sum_of_receiver = [[0 for _ in range(log_2_k + 1)] for _ in range(number_of_passers)]

        for u in range(number_of_passers):
            receiver[u][0] = next_receiver[u]
            sum_of_receiver[u][0] = u + next_receiver[u]

        for v in range(1, log_2_k + 1):
            for u in range(number_of_passers):
                first_receiver = receiver[u][v-1]
                receiver[u][v] = receiver[first_receiver][v-1]

                first_sum = sum_of_receiver[u][v-1] 
                second_sum = sum_of_receiver[first_receiver][v - 1]
                sum_of_receiver[u][v] = first_sum + second_sum - first_receiver
        
        power_of_two = [1 for _ in range(log_2_k + 1)]
        for i in range(1, log_2_k + 1):
            power_of_two[i] = 2 * power_of_two[i - 1]
        @lru_cache(maxsize=3400000)
        def calculate_passing_value(current_passer, j):
            if j == 0:
                return current_passer 

            if j == 1:
                return current_passer + next_receiver[current_passer]

            log_2_j = math.floor(math.log(j, 2))
            next_passer = receiver[current_passer][log_2_j]
            return sum_of_receiver[current_passer][log_2_j] + calculate_passing_value(next_passer, j - power_of_two[log_2_j]) - next_passer

        max_result = 0 
        for passer in range(number_of_passers):
            max_result = max(max_result, calculate_passing_value(passer, k))

        return max_result


if __name__ == '__main__':
    sol = Solution()
    receiver = [1,1,1,2,3]
    k = 3
    result = sol.getMaxFunctionValue(receiver, k)
    print(result)
        