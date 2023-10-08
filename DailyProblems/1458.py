from typing import List
from functools import lru_cache

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N1 = len(nums1)
        N2 = len(nums2)

        @lru_cache(maxsize=30000)
        def max_dot_product_dp(i: int, j: int) -> int:
            if i >= N1 or j >= N2:
                return 0

            option1 = max_dot_product_dp(i + 1, j)
            option2 = max_dot_product_dp(i, j + 1)
            option3 = max_dot_product_dp(i + 1, j + 1)
            option4 = nums1[i] * nums2[j] + max_dot_product_dp(i + 1, j + 1)

            return max(option1, option2, option3, option4)

        max_positive_dot_product = max_dot_product_dp(0, 0)

        if max_positive_dot_product == 0:
            max_negative_dot_product = nums1[0] * nums2[0]
            for i in range(N1):
                for j in range(N2):
                    max_negative_dot_product = max(nums1[i] * nums2[j], max_negative_dot_product)

            return max_negative_dot_product

        return max_positive_dot_product


if __name__ == '__main__':
    sol = Solution()
    nums1 = [-1]
    nums2 = [2, 3, 4]
    result = sol.maxDotProduct(nums1, nums2)
    print(result)