from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N + 1)]
        size = [1 for _ in range(N + 1)]

        def find_parent(i):
            if i != parent[i]:
                parent[i] = find_parent(parent[i])

            return parent[i]

        def union(u, v):
            pu = find_parent(u)
            pv = find_parent(v)

            if size[pu] < size[pv]:
                pu, pv = pv, pu

            size[pu] += size[pv]
            parent[pv] = pu

        for edge in edges:
            u, v = edge

            if find_parent(u) == find_parent(v):
                return edge

            union(u, v)


