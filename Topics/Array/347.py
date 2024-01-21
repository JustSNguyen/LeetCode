from typing import List 
from collections import defaultdict
import heapq 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        count = defaultdict(int)

        for num in nums:
            count[num] += 1 

        for num in count:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (count[num], num))
            elif count[num] > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (count[num], num)) 
        
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        
        return result 