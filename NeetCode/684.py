from typing import List 
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        temp_result = []
        for i in range(N):
            neighbors = defaultdict(list)
            for j in range(N):
                if j == i:
                    continue 

                u, v = edges[j]
                neighbors[u].append(v)
                neighbors[v].append(u)
            
            processed = set()
            stack = []
            stack.append(1)

            while stack:
                node = stack.pop()
                if node in processed:
                    continue 
                
                processed.add(node)
                for neighbor in neighbors[node]:
                    if neighbor not in processed:
                        stack.append(neighbor)
            
            if len(processed) == N:
                temp_result = edges[i]
            
        return temp_result