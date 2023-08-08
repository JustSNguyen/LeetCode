from typing import List 

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        nums_length = len(nums)
        can_be_splitted_subarray_dp_result = [[-1 for _ in range(nums_length)] for _ in range(nums_length)]

        def can_be_splitted_subarray_dp(i, j):
            if can_be_splitted_subarray_dp_result[i][j] != -1:
                return can_be_splitted_subarray_dp_result[i][j]

            if i == j:
                can_be_splitted_subarray_dp_result[i][j] = True 
                return True

            cur_prefix_sum = 0 
            subarray_length = j - i + 1
            subarray_sum = sum(nums[i: j + 1])

            for k in range(i, j):
                cur_prefix_sum += nums[k]
                cur_suffix_sum = subarray_sum - cur_prefix_sum
                cur_prefix_length = k - i + 1 
                cur_suffix_length = subarray_length - cur_prefix_length 

                qualified_prefix = False 
                qualified_suffix = False 

                if cur_prefix_length == 1 or cur_prefix_sum >= m:
                    qualified_prefix = True 
                
                if cur_suffix_length == 1 or cur_suffix_sum >= m:
                    qualified_suffix = True 
                
                if qualified_prefix and qualified_suffix:
                    prefix_can_be_splitted = can_be_splitted_subarray_dp(i, k)
                    suffix_can_be_splitted = can_be_splitted_subarray_dp(k + 1, j) 

                    if prefix_can_be_splitted and suffix_can_be_splitted:
                        can_be_splitted_subarray_dp_result[i][j] = True 
                        return True 
            
            can_be_splitted_subarray_dp_result[i][j] = False
            return False 
                
        return can_be_splitted_subarray_dp(0, nums_length - 1)

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    m = 6
    
    result = sol.canSplitArray(nums, m)

    print(result)