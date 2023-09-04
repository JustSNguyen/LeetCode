from typing import List
from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        reminder_count = defaultdict(int)
        reminder_count[0] = 1
        
        prefix_reminder_count = 0
        result = 0

        for num in nums:
            if num % modulo == k:
                prefix_reminder_count += 1

            reminder = prefix_reminder_count % modulo 

            adjusted_reminder = reminder - k 
            if adjusted_reminder < 0:
                adjusted_reminder += modulo

            result += reminder_count[adjusted_reminder]
            reminder_count[reminder] += 1

        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 4]
    modulo = 2
    k = 1
    result = sol.countInterestingSubarrays(nums, modulo, k)
    print(result)
