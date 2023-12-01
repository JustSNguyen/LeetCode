from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        N = len(time)

        neighbors = defaultdict(list)
        for relation in relations:
            prev, next = relation
            neighbors[next].append(prev)

        @lru_cache(maxsize=N)
        def get_time_to_finish(index: int) -> int:
            prev_courses_time = 0
            for neighbor in neighbors[index]:
                prev_courses_time = max(prev_courses_time, get_time_to_finish(neighbor))

            return prev_courses_time + time[index - 1]

        result = 0
        for i in range(1, n + 1):
            result = max(result, get_time_to_finish(i))

        return result

