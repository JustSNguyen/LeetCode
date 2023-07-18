from typing import List 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur_index = 0 
        nums_length = len(nums) 

        while cur_index < nums_length:
            if nums[cur_index] == cur_index or nums[cur_index] >= nums_length: 
                cur_index += 1 
                continue 

            while nums[cur_index] != cur_index and nums[cur_index] < nums_length:
                current_number = nums[cur_index]
                num_in_correct_position = nums[current_number]
                nums[cur_index], nums[current_number] = num_in_correct_position, current_number
            
            cur_index += 1 
        
        for i in range(0, nums_length):
            if nums[i] != i: return i 
        
        return nums_length

if __name__ == "__main__":
    sol = Solution()
    nums = [3,0,1]
    missing_number = sol.missingNumber(nums)
    print(missing_number)
                