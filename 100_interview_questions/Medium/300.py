from typing import List 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find_smaller_or_equal_to_num(num_list, num):
            lf = 0 
            rg = len(num_list)

            while lf < rg: 
                

        current_lis = []
        for num in nums:
            if len(current_lis) == 0 or num > current_lis[-1]:
                current_lis.append(num)
            
            else:
