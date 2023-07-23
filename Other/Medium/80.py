from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous_num = nums[0]
        count_nums = 0 
        cur_result_length = 0 

        for i, num in enumerate(nums):
            if num == previous_num:
                count_nums += 1 
            else: 
                count_nums = 1 
            
            if count_nums <= 2:
                nums[i], nums[cur_result_length] = nums[cur_result_length], nums[i]
                cur_result_length += 1

            previous_num = num 

        print(nums)
        return cur_result_length    

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 1]
    result = sol.removeDuplicates(nums)
    print(result)