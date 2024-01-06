from typing import List 

class Solution:
    def findOrder(self, N: int, edges: List[List[int]]) -> List[int]:
        colors = [0 for _ in range(N)]
        neighbors = [[] for _ in range(N)]
        indegrees = [0 for _ in range(N)]
        result = []

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
            result.append(node)
            return False 
        
        for edge in edges:
            u, v = edge 
            neighbors[v].append(u)
            indegrees[u] += 1 
        
        for node in range(N):
            if indegrees[node] == 0:
                if dfs(node):
                    return []
        
        for color in colors:
            if color != 2:
                return []
        
        return list(reversed(result))