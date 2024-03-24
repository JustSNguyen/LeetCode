from typing import List 
from collections import deque 
import bisect

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        increasing_queue_by_value = deque()
        increasing_queue_by_index = deque()
        
        increasing_queue_by_value.append(0)
        increasing_queue_by_index.append(-1)

        prefix = 0 
        shortest = len(nums) + 1 

        for i, num in enumerate(nums):
            prefix += num 
            while increasing_queue_by_index and increasing_queue_by_index[0] < i - shortest:
                increasing_queue_by_index.popleft()
                increasing_queue_by_value.popleft()

            if increasing_queue_by_value and increasing_queue_by_value[0] <= prefix - k:
                j1 = bisect.bisect_right(increasing_queue_by_value, prefix - k) - 1 
                j2 = increasing_queue_by_index[j1]
                shortest = min(shortest, i - j2)

            while increasing_queue_by_value and increasing_queue_by_value[-1] >= prefix:
                increasing_queue_by_value.pop()
                increasing_queue_by_index.pop()
            
            increasing_queue_by_value.append(prefix)
            increasing_queue_by_index.append(i)
        
        if shortest > len(nums):
            return -1 
        
        return shortest 

if __name__ == '__main__':
    sol = Solution()
    test = [48,99,37,4,-31]
    k = 140
    result = sol.shortestSubarray(test, k)
    print(result)