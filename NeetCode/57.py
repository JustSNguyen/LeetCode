from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        for i, interval in enumerate(intervals):
            if interval[0] > new_interval[1]:
                if not inserted:
                    result.append(new_interval)
                    inserted = True

                result.append(interval)

            elif interval[1] < new_interval[0]:
                result.append(interval)

            else:
                new_interval = [min(new_interval[0], interval[0]), max(interval[1], new_interval[1])]

        if not inserted:
            result.append(new_interval)

        return result

if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,2], [9, 11]]
    newInterval = [3, 5]
    result = sol.insert(intervals, newInterval)
    print(result)

