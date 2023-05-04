from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consecutive_start_at_result = {num: -1 for num in nums}
        def longest_consecutive_start_at(num):
            if longest_consecutive_start_at_result[num] != -1:
                return longest_consecutive_start_at_result[num]
            
            cur_result = 1
            next_num = num + 1 
            if next_num not in longest_consecutive_start_at_result:
                longest_consecutive_start_at_result[num] = 1
                return longest_consecutive_start_at_result[num]
            
            cur_result = 1 + longest_consecutive_start_at(next_num)
            longest_consecutive_start_at_result[num] = cur_result
            return longest_consecutive_start_at_result[num]
        
        longest_consecutive_result = 0
        for num in longest_consecutive_start_at_result:
            longest_consecutive_result = max(longest_consecutive_result, longest_consecutive_start_at(num))

        return longest_consecutive_result
    
if __name__ == "__main__":
    nums = []
    sol = Solution()
    print(sol.longestConsecutive(nums))
