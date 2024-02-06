from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        M = len(matrix)
        N = len(matrix[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_direction_index = 0
        visited = [[False for _ in range(N)] for _ in range(M)]

        i = 0 
        j = 0 

        while len(result) != M * N:
            while True:
                result.append(matrix[i][j])
                visited[i][j] = True 

                ni, nj = i + directions[cur_direction_index][0], j + directions[cur_direction_index][1]

                if ni < 0 or nj < 0 or ni >= M or nj >= N or visited[ni][nj]:
                    break 

   
                i = ni 
                j = nj 
            
            cur_direction_index = cur_direction_index + 1 if cur_direction_index != len(directions) - 1 else 0 
            ni, nj = i + directions[cur_direction_index][0], j + directions[cur_direction_index][1] 
            i = ni 
            j = nj
        
        return result 

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]] 
    result = sol.spiralOrder(matrix)
    print(result)
