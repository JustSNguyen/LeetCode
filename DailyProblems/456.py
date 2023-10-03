from typing import List
from functools import lru_cache

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)

        if N < 3:
            return False

        min_number_from_start_to_index = [nums[0] for _ in range(N)]
        stack = []
        for k in range(N):
            if k >= 0:
                min_number_from_start_to_index[k] = min(min_number_from_start_to_index[k - 1], nums[k])

            while stack and nums[stack[-1]] <= nums[k]:
                stack.pop()

            if stack:
                j = stack[-1]

                if j > 0:
                    min_number = min_number_from_start_to_index[j - 1]
                    if min_number < nums[k] < nums[j]:
                        return True

            stack.append(k)

        return False



if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 3, 2, 0]
    result = sol.find132pattern(nums)
    print(result)



