import heapq

from typing import List
from collections import defaultdict

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.INF = 10**9
        self.edges = edges
        self.N = n
        self.neighbors = defaultdict(list)

        for edge in edges:
            u, v, w = edge
            self.neighbors[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        self.edges.append(edge)

        u, v, w = edge
        self.neighbors[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        min_heap = []
        dist = [self.INF for _ in range(self.N)]
        dist[node1] = 0
        heapq.heappush(min_heap, (0, node1))
        processed = set()

        while min_heap:
            weight, cur = heapq.heappop(min_heap)

            if cur in processed:
                continue

            processed.add(cur)

            for neighbor, weight in self.neighbors[cur]:
                if dist[cur] + weight < dist[neighbor]:
                    dist[neighbor] = dist[cur] + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))

        if dist[node2] == self.INF:
            return -1

        return dist[node2]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)