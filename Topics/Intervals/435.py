from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[1])
        result = 0

        i = 0
        N = len(intervals)
        while i < len(intervals):
            interval = intervals[i]
            ni = N
            for j in range(i + 1, N):
                if intervals[j][0] >= interval[1]:
                    ni = j
                    break

            result += (ni - i - 1)
            i = ni

        return result


if __name__ == '__main__':
    test = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    sol = Solution()
    result = sol.eraseOverlapIntervals(test)
    print(result)