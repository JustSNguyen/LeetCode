import math

class Solution:
    def poorPigs(self, N: int, minutes_to_die: int, minutes_to_test: int) -> int:
        M = minutes_to_test // minutes_to_die
        if M == 1:
            return N - 2

        return

if __name__ == '__main__':
    sol = Solution()
    N = 1000
    minutes_to_test = 60
    minutes_to_die = 15
    print(sol.poorPigs(N, minutes_to_die, minutes_to_test))