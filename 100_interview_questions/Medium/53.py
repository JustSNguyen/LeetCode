from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        NEG_INF = -10**12
        nums_length = len(nums)
        max_sub_array_from_result = [NEG_INF for _ in range(nums_length)]

        def max_sub_array_from(index):
            if index >= nums_length:
                return 0 
            
            if max_sub_array_from_result[index] != NEG_INF:
                return max_sub_array_from_result[index]
            
            cur_num = nums[index]
            max_sub_array_from_result[index] = max(cur_num, cur_num + max_sub_array_from(index + 1))

            return max_sub_array_from_result[index]
        
        max_result = NEG_INF
        for i in range(nums_length):
            max_result = max(max_result, max_sub_array_from(i))
        
        return max_result

if __name__ == "__main__":
    nums = [-2]
    sol = Solution()
    print(sol.maxSubArray(nums))