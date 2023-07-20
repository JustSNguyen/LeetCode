from typing import List 
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        min_heap = []

        for i in range(min(k, m)):
            cur_tuple = (matrix[i][0], i, 0)
            heapq.heappush(min_heap, cur_tuple)
        
        ans = -1 
        for i in range(k):
            ans, row, col = heapq.heappop(min_heap)
            
            if col + 1 < n: 
                cur_tuple = (matrix[row][col + 1], row, col + 1)
                heapq.heappush(min_heap, cur_tuple)
        
        return ans 
    
if __name__ == "__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    sol = Solution()
    print(sol.kthSmallest(matrix, k))