from typing import List
from collections import deque, defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adj = defaultdict(list)

        for ticket in tickets:
            u, v = ticket
            adj[u].append(v)

        result = deque()
        def dfs(start):
            while adj[start]:
                dfs(adj[start].pop())

            result.appendleft(start)

        dfs("JFK")
        return list(result)