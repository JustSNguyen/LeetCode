from typing import List
from collections import deque, defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        dest = defaultdict(list)
        tickets = sorted(tickets, reverse=True)

        for ticket in tickets:
            u, v = ticket
            dest[u].append(v)

        orders = deque()
        def dfs(start):
            while dest[start]:
                next = dest[start].pop()
                dfs(next)

            orders.appendleft(start)

        dfs("JFK")
        return list(orders)

if __name__ == '__main__':
    sol = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    result = sol.findItinerary(tickets)
    print(result)