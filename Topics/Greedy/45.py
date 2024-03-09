from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest_position = 0
        N = len(nums)
        min_steps = [0 for _ in range(N)]

        for i, num in enumerate(nums):
            temp = min(i + num, len(nums) - 1)
            if temp > furthest_position:
                for j in range(furthest_position + 1, temp + 1):
                    min_steps[j] = min_steps[i] + 1

                furthest_position = temp

        return min_steps[N - 1]


if __name__ == '__main__':
    sol = Solution()
    test = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    result = sol.jump(test)
    print(result)
