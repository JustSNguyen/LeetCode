from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        new_intervals = []

        for i, interval in enumerate(intervals):
            if interval[1] < new_interval[0]:
                new_intervals.append(interval)

            elif interval[0] > new_interval[1]:
                new_intervals.append(new_interval)
                new_intervals.extend(intervals[i:])
                return new_intervals

            else:
                new_interval = merge(new_interval, interval)

        new_intervals.append(new_interval)
        return new_intervals


