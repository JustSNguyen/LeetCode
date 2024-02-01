from typing import List
import math

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n + 1):
            xor ^= i

        for num in nums:
            xor ^= num

        print(30 ^ 0)
        return xor

if __name__ == '__main__':
    sol = Solution()
    nums = [3,0,1]
    result = sol.missingNumber(nums)
    print(result)
