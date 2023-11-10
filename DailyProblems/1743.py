from typing import List
from collections import defaultdict

class Solution:
    def restoreArray(self, adjacent_pairs: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)
        NEG_INF = -10**6

        for pair in adjacent_pairs:
            u, v = pair
            neighbors[u].append(v)
            neighbors[v].append(u)

        start_of_array = 0
        for node in neighbors:
            if len(neighbors[node]) == 1:
                start_of_array = node
                break

        stack = [(start_of_array, NEG_INF)]
        result = []
        while stack:
            cur_node, parent_of_cur_node = stack.pop()

            result.append(cur_node)

            for neighbor in neighbors[cur_node]:
                if neighbor != parent_of_cur_node:
                    stack.append((neighbor, cur_node))

        return result