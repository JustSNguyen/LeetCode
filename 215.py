from typing import List

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_kth_largest_helper(nums, k):
            N = len(nums)

            if N == 1:
                return nums[0]

            pivot_index = random.randint(0, N - 1)
            pivot = nums[pivot_index]
            larger_than_pivot_nums = []
            equal_to_pivot_nums = []
            smaller_than_pivot_nums = []
            for _, num in enumerate(nums):
                if num > pivot:
                    larger_than_pivot_nums.append(num)
                elif num == pivot:
                    equal_to_pivot_nums.append(num)
                else:
                    smaller_than_pivot_nums.append(num)

            larger_than_pivot_nums_length = len(larger_than_pivot_nums)
            equal_to_pivot_nums_length = len(equal_to_pivot_nums)

            if larger_than_pivot_nums_length >= k: 
                return find_kth_largest_helper(larger_than_pivot_nums, k)
            
            if larger_than_pivot_nums_length + equal_to_pivot_nums_length < k: 
                return find_kth_largest_helper(smaller_than_pivot_nums, 
                k - larger_than_pivot_nums_length - equal_to_pivot_nums_length)
            
            return pivot
        
        return find_kth_largest_helper(nums, k)

if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 1]
    k = 2
    print(sol.findKthLargest(nums, k))
            
