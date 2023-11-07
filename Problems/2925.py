from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        N = len(values)

        neighbors = defaultdict(list)
        for edge in edges:
            u, v = edge
            neighbors[u].append(v)
            neighbors[v].append(u)

        children = defaultdict(list)
        processed = set()
        stack = [0]
        while stack:
            cur = stack.pop()
            if cur in processed:
                continue

            processed.add(cur)

            for node in neighbors[cur]:
                if node not in processed:
                    children[cur].append(node)
                    stack.append(node)

        @lru_cache(maxsize=2*N)
        def get_max_score(root, is_zero):
            if not is_zero:
                score = values[root]
                for child in children[root]:
                    score += get_max_score(child, is_zero)
                return score

            elif len(children[root]) == 0:
                return 0

            else:
                max_score = 0
                for new_is_zero in [False, True]:
                    score = 0
                    if new_is_zero:
                        score = values[root]

                    for child in children[root]:
                        score += get_max_score(child, new_is_zero)

                    max_score = max(max_score, score)
                return max_score

        return get_max_score(0, True)