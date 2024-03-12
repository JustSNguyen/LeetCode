# Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
# find the minimum number of conference rooms required.

# Input:
# [[0, 30],[5, 10],[15, 20]]
# Output:
# 2

# Input:
# [[7,10],[2,4]]
# Output:
# 1

import heapq
def solve(intervals):
    if not intervals:
        return 0

    intervals.sort()
    end_times = []
    max_at_one_time = 0

    for intervals in intervals:
        if end_times and intervals[0] >= end_times[0]:
            heapq.heappop(end_times)

        heapq.heappush(end_times, intervals[1])

        max_at_one_time = max(max_at_one_time, len(end_times))

    return max_at_one_time

inputs = [
    [[0, 30],[5, 10],[15, 20]],
    [[7,10],[2,4]],
    [],
    [[2,5]]
]

outputs = [
    2,
    1,
    0,
    1
]

for i, input in enumerate(inputs):
    result = solve(input)
    print(result, outputs[i])
    break
