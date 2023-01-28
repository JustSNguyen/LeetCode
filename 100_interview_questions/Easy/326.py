class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**20 % n == 0 

if __name__ == '__main__':
    n = 27
    sol = Solution()
    print(sol.isPowerOfThree(n))