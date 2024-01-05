from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        dp_max_i_plus_1 = 1
        dp_min_i_plus_1 = 1
        max_product = nums[-1]

        for i in range(N - 1, - 1, -1):
            if nums[i] < 0:
                dp_max = max(nums[i], nums[i] * dp_min_i_plus_1)
                dp_min = min(nums[i], nums[i] * dp_max_i_plus_1)
            else:
                dp_max = max(nums[i], nums[i] * dp_max_i_plus_1)
                dp_min = min(nums[i], nums[i] * dp_min_i_plus_1)

            max_product = max(max_product, dp_max)

            dp_min_i_plus_1 = dp_min
            dp_max_i_plus_1 = dp_max

        return max_product

if __name__ == '__main__':
    sol = Solution()
    nums = [-3,-1,-1]
    result = sol.maxProduct(nums)
    print(result)

