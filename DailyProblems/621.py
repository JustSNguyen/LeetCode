from typing import List
from collections import defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = defaultdict(int)
        for task in tasks:
            task_frequency[task] += 1

        max_heap = []
        for task in task_frequency:
            heapq.heappush(max_heap, -task_frequency[task])

        total = 0
        while True:
            tasks_in_an_interval = 0
            new_task_cnt = []
            while max_heap and tasks_in_an_interval != (n + 1):
                task_cnt = -heapq.heappop(max_heap)
                tasks_in_an_interval += 1
                task_cnt -= 1
                if task_cnt > 0:
                    new_task_cnt.append(task_cnt)
                total += 1

            if not new_task_cnt and not max_heap:
                return total

            total += (n + 1 - tasks_in_an_interval)

            for task_cnt in new_task_cnt:
                heapq.heappush(max_heap, -task_cnt)





