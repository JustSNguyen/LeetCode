from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)

        product_from_start = [1 for _ in range(nums_length)]
        for i, num in enumerate(nums):
            if i == 0:
                product_from_start[i] = num 
                continue 

            product_from_start[i] = product_from_start[i - 1] * num 

        product_from_end = [1 for _ in range(nums_length)]
        for i in range(nums_length - 1, -1, -1):
            if i == nums_length - 1:
                product_from_end[i] = num 
                continue 

            product_from_end[i] = product_from_end[i + 1] * nums[i]

        result = [1 for _ in range(nums_length)]
        for i in range(nums_length):
            if i == 0: result[i] = product_from_end[1] 
            elif i == nums_length - 1: result[i] = product_from_start[i - 1]
            else: result[i] = product_from_start[i - 1] * product_from_end[i + 1]
        
        return result 

if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))