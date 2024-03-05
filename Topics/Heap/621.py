from typing import List
from collections import defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        total = 0
        completed_tasks = 0
        cnt = defaultdict(int)
        for task in tasks:
            cnt[task] += 1

        for task in cnt:
            value = cnt[task]
            heapq.heappush(max_heap, (-value, task))

        while completed_tasks != len(tasks):
            tasks_need_to_process = 0
            temp = []
            while max_heap and tasks_need_to_process != n + 1:
                negative_task_count, task_name = heapq.heappop(max_heap)
                new_task_count = -negative_task_count - 1

                tasks_need_to_process += 1

                if new_task_count > 0:
                    temp.append((-new_task_count, task_name))

                completed_tasks += 1

                total += 1

            if len(temp) != 0:
                total += (n + 1 - tasks_need_to_process)

            for t in temp:
                heapq.heappush(max_heap, t)

        return total

