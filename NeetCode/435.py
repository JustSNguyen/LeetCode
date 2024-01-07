from typing import List
import bisect 

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals = sorted(intervals)
        dp = [0 for _ in range(N + 1)]
        MIN_VALUE = -10**12

        for i in range(N - 1, -1, -1):
            first_option = dp[i + 1] + 1 
            interval = intervals[i]
            j = bisect.bisect_left(intervals, [interval[1], MIN_VALUE])
            second_option = dp[j] + (j - i - 1)
            dp[i] = min(first_option, second_option)
        
        return dp[0]

if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,2],[2,3],[3,4],[1,3]]