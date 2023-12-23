class Solution:
    def isPathCrossing(self, path: str) -> bool:
        offsets = {
            "N": [0, 1],
            "E": [1, 0],
            "S": [0, -1],
            "W": [-1, 0]
        }

        visited = set()

        current = (0, 0)
        visited.add(current)
        for direction in path:
            offset = offsets[direction]
            new_x = current[0] + offset[0]
            new_y = current[1] + offset[1]

            if (new_x, new_y) in visited:
                return True 
            
            visited.add((new_x, new_y))

            current = (new_x, new_y)
        
        return False 

if __name__ == '__main__':
    sol = Solution()
    path = "NESWW"
    result = sol.isPathCrossing(path)
    print(result)