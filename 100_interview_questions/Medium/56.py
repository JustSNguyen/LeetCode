from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = list(sorted(intervals))
        result = []
        current_interval = []

        for interval in sorted_intervals:
            if len(current_interval) == 0:
                current_interval = interval
            
            else:
                start, end = current_interval
                if end < interval[0]:
                    result.append(current_interval)
                    current_interval = interval
                else:
                    current_interval = [start, max(end, interval[1])]
        
        result.append(current_interval)

        return result

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,4], [4,5]]
    result = sol.merge(intervals)
    print(result)