from typing import List 

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count_combination_dp_result = [[-1 for _ in range(len(nums))] for _ in range(target + 1)]

        def count_combination_dp(cur_sum, num_index):
            if cur_sum == 0:
                return 1
            
            if cur_sum < 0:
                return 0

            cur_num = nums[num_index]
            if num_index == 0:
                print(cur_sum, cur_num)
                if cur_sum % cur_num != 0: return 0 
                return 1

            if count_combination_dp_result[cur_sum][num_index] != -1:
                return count_combination_dp_result[cur_sum][num_index]

            return count_combination_dp(cur_sum - cur_num, num_index) + count_combination_dp(cur_sum, num_index - 1)
        

        return count_combination_dp(target, len(nums) - 1)

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 1, 2]
    target = 4
    print(sol.combinationSum4(nums, target))