from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(maxsize = 20000)
        def count_unique_paths_dp(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return 0 
            
            if i == m - 1 and j == n - 1:
                return 1 
            
            return count_unique_paths_dp(i + 1, j) + count_unique_paths_dp(i, j + 1)

        return count_unique_paths_dp(0, 0) 
    
if __name__ == '__main__':
    sol = Solution()
    m = 1
    n = 1 
    result = sol.uniquePaths(m, n)
    print(result)