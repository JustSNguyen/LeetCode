from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0 for _ in range(n)]

        for edge in edges:
            u, v = edge
            in_degree[v] += 1

        number_of_nodes_with_zero_indegree = 0
        node_with_zero_indegree = 0
        for i in range(n):
            if in_degree[i] == 0:
                number_of_nodes_with_zero_indegree += 1
                node_with_zero_indegree = i

            if number_of_nodes_with_zero_indegree > 1:
                return -1

        return node_with_zero_indegree
