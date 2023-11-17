from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = list(sorted(arr))
        arr[0] = 1
        N = len(arr)
        max_so_far = 1

        prev = arr[0]
        for i in range(1, N):
            diff = abs(prev - arr[i])

            if diff > 1:
                prev += 1
            else:
                prev = arr[i]

            max_so_far = max(max_so_far, prev)

        return max_so_far