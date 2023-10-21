from functools import lru_cache

class Solution:
    def numWays(self, steps: int, arr_length: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(maxsize=steps*steps)
        def count_number_of_ways(index: int, steps_available: int) -> int:
            if steps_available == 0 and index == 0:
                return 1

            if steps_available == 0:
                return 0

            first_option = 0
            if index < arr_length - 1:
                first_option = count_number_of_ways(index + 1, steps_available - 1) % MOD

            second_option = count_number_of_ways(index, steps_available - 1) % MOD

            third_option = 0
            if index >= 1:
                third_option = count_number_of_ways(index - 1, steps_available - 1) % MOD

            return (((first_option + second_option) % MOD) + third_option) % MOD

        return count_number_of_ways(0, steps)

if __name__ == '__main__':
    sol = Solution()
    steps = 1
    arr_length = 1
    result = sol.numWays(steps, arr_length)
    print(result)