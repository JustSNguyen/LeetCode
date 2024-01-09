from typing import List 
from collections import deque 

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing_queue = deque()
        decreasing_queue = deque()
        left = 0 
        max_length = 0 

        for i, num in enumerate(nums):
            while increasing_queue and num < nums[increasing_queue[-1]]:
                increasing_queue.pop()
            increasing_queue.append(i)

            while decreasing_queue and num > nums[decreasing_queue[-1]]:
                decreasing_queue.pop()
            decreasing_queue.append(i)

            while nums[decreasing_queue[0]] - nums[increasing_queue[0]] > limit:
                left += 1 

                while increasing_queue[0] < left:
                    increasing_queue.popleft()
            
                while decreasing_queue[0] < left:
                    decreasing_queue.popleft()
            
            max_length = max(max_length, i - left + 1)
        
        return max_length


if __name__ == '__main__':
    sol = Solution()
    test = [8, 2, 4, 7]
    limit = 4
    result = sol.longestSubarray(test, limit)
    print(result)            
