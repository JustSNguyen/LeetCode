class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cur_power_of_four = 1
        while cur_power_of_four <= n:
            if cur_power_of_four == n:
                return True

            cur_power_of_four *= 4

        return False

