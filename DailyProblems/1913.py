from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        MAX = 10**5
        MIN = 0

        min_pair = [MAX, MAX]
        max_pair = [MIN, MIN]

        for num in nums:
            if num > max_pair[0]:
                max_pair[1] = max_pair[0]
                max_pair[0] = num
            elif num > max_pair[1]:
                max_pair[1] = num

            if num < min_pair[0]:
                min_pair[1] = min_pair[0]
                min_pair[0] = num
            elif num < min_pair[1]:
                min_pair[1] = num

        return (max_pair[0] * max_pair[1]) - (min_pair[0] * min_pair[1])

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, 5, 5]
    result = sol.maxProductDifference(nums)
    print(result)
