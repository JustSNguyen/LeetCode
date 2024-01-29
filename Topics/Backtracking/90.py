from typing import List
from collections import defaultdict

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        result = []
        distinct_nums = list(count.keys())

        def generate(temp, index):
            if index == len(distinct_nums):
                result.append(temp)
                return

            num = distinct_nums[index]
            for i in range(count[num] + 1):
                new_temp = temp[:]
                new_temp.extend([num] * i)
                generate(new_temp, index + 1)

        generate([], 0)
        return result

if __name__ == '__main__':
    sol = Solution()
    test = [1, 2, 2]
    result = sol.subsetsWithDup(test)
    print(result)