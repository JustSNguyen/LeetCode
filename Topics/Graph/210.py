from typing import List
from collections import defaultdict, deque
class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        WHITE = 0
        GREY = 1
        BLACK = 2

        colors = [WHITE for _ in range(N)]
        orders = deque()
        adj = defaultdict(list)

        for prerequisite in prerequisites:
            u, v = prerequisite
            adj[v].append(u)

        def dfs(node):
            if colors[node] == GREY:
                raise Exception("Cycle")

            if colors[node] == BLACK:
                return

            colors[node] = GREY
            for neighbor in adj[node]:
                dfs(neighbor)

            colors[node] = BLACK

            orders.appendleft(node)

        for node in range(N):
            try:
                dfs(node)
            except:
                return []

        return list(orders)


