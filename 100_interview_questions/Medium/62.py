class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        number_of_unique_paths = [[-1 for _ in range(n)] for _ in range(m)]
        number_of_unique_paths[m - 1][n - 1] = 1 
        def count_unique_paths(i, j):
            if i >= m or i < 0 or j >= n or j < 0: 
                return 0 

            if number_of_unique_paths[i][j] != -1 :
                return number_of_unique_paths[i][j]
            
            number_of_unique_paths[i][j] = count_unique_paths(i + 1, j) + count_unique_paths(i, j + 1)

            return number_of_unique_paths[i][j]
        
        return count_unique_paths(0, 0)
    
if __name__ == '__main__':
    sol = Solution()
    m = 3 
    n = 2
    print(sol.uniquePaths(m, n))