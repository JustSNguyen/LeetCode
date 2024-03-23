import heapq 
from typing import List 

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = list(sorted(intervals, reverse=True))

        Q = len(queries)
        queries = [(queries[i], i) for i in range(Q)]
        result = [-1 for _ in range(Q)]

        queries.sort()

        min_heap = []
        for query, index in queries: 
            while intervals and intervals[-1][0] <= query:
                i, j = intervals.pop()
                if j >= query:
                    length = j - i + 1 
                    heapq.heappush(min_heap, [length, j])
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[index] = min_heap[0][0]
        
        return result 