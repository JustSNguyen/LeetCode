from typing import List
from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        rows = []

        for num in nums:
            count[num] += 1

            if count[num] > len(rows):
                rows.append([num])
            else:
                rows[count[num] - 1].append(num)

        return rows

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,4,1,2,3,1]
    result = sol.findMatrix(nums)
    print(result)