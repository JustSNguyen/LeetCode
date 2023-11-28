from typing import List
from collections import defaultdict

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)

        count = defaultdict(int)
        for i in range(n):
            if arr[i] > n:
                count[n] += 1
            else:
                count[arr[i]] += 1

        for i in range(2, n + 1):
            count[i] += count[i - 1]

        new_arr = [0] * n
        for num in arr:
            if num > n:
                num = n

            new_arr[count[num] - 1] = num
            count[num] -= 1

        new_arr[0] = 1
        max_so_far = 1

        prev = new_arr[0]
        for i in range(1, n):
            diff = abs(prev - new_arr[i])

            if diff > 1:
                new_arr[i] = prev + 1

            prev = new_arr[i]

            max_so_far = max(max_so_far, new_arr[i])

        return max_so_far
    
