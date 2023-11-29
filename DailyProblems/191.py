class Solution:
    def hammingWeight(self, n: int) -> int:
        number_of_one_bits = 0

        while n:
            n &= (n - 1)
            number_of_one_bits += 1

        return number_of_one_bits


if __name__ == '__main__':
    sol = Solution()
    result = sol.hammingWeight(10)
