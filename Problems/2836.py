import math
from typing import List

class Solution:
    def getMaxFunctionValue(self, next_receiver: List[int], k: int) -> int:
        log_2_k = math.floor(math.log(k, 2))
        number_of_passers = len(next_receiver)
        receiver = [[0 for _ in range(log_2_k + 1)] for _ in range(number_of_passers)]

        for u in range(number_of_passers):
            receiver[u][0] = next_receiver[u]

        for v in range(1, log_2_k + 1):
            for u in range(number_of_passers):
                receiver[u][v] = receiver[receiver[u][v - 1]][v - 1]


        def calculate_passing_value(current_passer, j):
            if j == 0:
                return current_passer 

            if j == 1:
                return current_passer + next_receiver[current_passer]

            for next_j in range(log_2_k, -1, -1):
                if 2 ** next_j < j:
                    next_passer = receiver[current_passer][next_j]
                    return calculate_passing_value(current_passer, 2 ** next_j) + calculate_passing_value(receiver[next_passer][0], j - 2 ** next_j - 1) 
                    
        
        return calculate_passing_value(2, 4)


        

if __name__ == '__main__':
    sol = Solution()
    receiver = [2,0,1]
    k = 5
    result = sol.getMaxFunctionValue(receiver, k)
    print(result)
        