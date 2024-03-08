from typing import List
from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        max_cnt = 0
        for num in nums:
            cnt[num] += 1
            max_cnt = max(max_cnt, cnt[num])

        result = 0
        for num in nums:
            if cnt[num] == max_cnt:
                result += 1

        return result