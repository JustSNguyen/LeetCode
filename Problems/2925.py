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

        @lru_cache(maxsize=2 * N)
        def get_max_score(root, parent, is_zero):
            if not is_zero:
                score = values[root]
                for child in neighbors[root]:
                    if child == parent:
                        continue

                    score += get_max_score(child, root, is_zero)
                return score

            elif len(neighbors[root]) == 1 and root != 0:
                return 0

            else:
                max_score = 0
                for new_is_zero in [False, True]:
                    score = 0
                    if new_is_zero:
                        score = values[root]

                    for child in neighbors[root]:
                        if child == parent:
                            continue

                        score += get_max_score(child, root, new_is_zero)

                    max_score = max(max_score, score)
                return max_score

        return get_max_score(0, -1, True)

if __name__ == '__main__':
    sol = Solution()
    edges = [[0,1]]
    values = [1,2]
    result = sol.maximumScoreAfterOperations(edges, values)
    print(result)