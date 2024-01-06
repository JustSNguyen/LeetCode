from typing import List 

class Solution:
    def canFinish(self, N: int, edges: List[List[int]]) -> bool:
        colors = [0 for _ in range(N)]
        indegrees = [0 for _ in range(N)]
        neighbors = [[] for _ in range(N)]

        def dfs(node):
            if colors[node] == 1:
                return True 
            
            if colors[node] == 2:
                return False 
            
            colors[node] = 1 

            for neighbor in neighbors[node]:
                if dfs(neighbor):
                    return True 
            
            colors[node] = 2 
            return False

        for edge in edges:
            u, v = edge 
            neighbors[v].append(u)
            indegrees[u] += 1 

        for node in range(N):
            if indegrees[node] == 0:
                has_cyle = dfs(node)
                found = True 
                if has_cyle:
                    return False 
                
        for color in colors:
            if color == 0:
                return False 

        return True
        