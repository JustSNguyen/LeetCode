from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def can_be_merged(interval1, interval2):
            return interval1[0] <= interval2[0] <= interval1[1] or interval2[0] <= interval1[0] <= interval2[1]

        if not intervals:
            return intervals

        intervals.sort()

        prev_interval = intervals[0]
        new_intervals = []

        for interval in intervals:
            if can_be_merged(interval, prev_interval):
                prev_interval = [min(prev_interval[0], interval[0]), max(prev_interval[1], interval[1])]
            else:
                new_intervals.append(prev_interval)
                prev_interval = interval

        new_intervals.append(prev_interval)

        return new_intervals
