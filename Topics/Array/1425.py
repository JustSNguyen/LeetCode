from collections import deque
from typing import List 

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        decreasing_queue = deque()
        max_value = nums[0]

        for i, num in enumerate(nums):
            while decreasing_queue and decreasing_queue[0][0] < i - k:
                decreasing_queue.popleft()
            
            max_value_in_range = decreasing_queue[0][1] if decreasing_queue else 0 
            max_value_in_range = max(max_value_in_range, 0)
            temp = max_value_in_range + num 
            max_value = max(max_value, temp)

            while decreasing_queue and decreasing_queue[-1][1] < temp:
                decreasing_queue.pop()
            decreasing_queue.append((i, temp))

        return max_value

if __name__ == '__main__':
    sol = Solution()
    test = [10,2,-10,5,20]
    k = 2
    result = sol.constrainedSubsetSum(test, k)
    print(result)