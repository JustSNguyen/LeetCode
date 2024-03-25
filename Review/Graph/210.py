from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        if N == 0:
            return []

        adj = defaultdict(list)
        in_degree = dict()

        for node in range(N):
            in_degree[node] = 0

        for second, first in prerequisites:
            adj[first].append(second)
            in_degree[second] += 1

        colors = defaultdict(int)

        def has_cycle(node):
            if colors[node] == 1:
                return True

            if colors[node] == 2:
                return False

            colors[node] = 1
            for neigh in adj[node]:
                if has_cycle(neigh):
                    return True

            colors[node] = 2
            return False

        result = []
        visited = set()
        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    dfs(neigh)

            result.append(node)

        for node in in_degree:
            if in_degree[node] == 0:
                if has_cycle(node):
                    return []

                dfs(node)

        if len(result) != N:
            return []

        return result[::-1]


if __name__ == '__main__':
    sol = Solution()
    test = [[1,0],[2,0],[3,1],[3,2]]
    result = sol.findOrder(4, test)
    print(result)
