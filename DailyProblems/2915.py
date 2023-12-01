from typing import List

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [[N + 1 for _ in range(target + 1)] for _ in range(N)]

        def get_longest_subsequence_at_index(i, target):
            if target == 0:
                return 0

            if i == N:
                return -2 * N

            if dp[i][target] != N + 1:
                return dp[i][target]

            if nums[i] > target:
                dp[i][target] = get_longest_subsequence_at_index(i + 1, target)
                return dp[i][target]

            option1 = get_longest_subsequence_at_index(i + 1, target)
            option2 = get_longest_subsequence_at_index(i + 1, target - nums[i]) + 1
            dp[i][target] = max(option1, option2)
            return dp[i][target]

        result = get_longest_subsequence_at_index(0, target)
        if result < 0:
            return - 1
        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [57,63,10,5,20,56,92,26,33,61,90,83,5,4,36,8,52,94,82,29,5,74,67,20,37,85,46,84,18,82,3,82,54,94,22,20,12,90,86,87,39,85,36,46,37,22,25,55,80,24,81,7,90,8,97,73,23,21,83,9,66,2,53,57,29,25,69,66,87,25,33,20,50,12,36,28,66,14,51,78,30,29,62,9,16,34,2,77,64,30,84,20,92,83,91,83,72,75,87,16]
    target = 602
    result = sol.lengthOfLongestSubsequence(nums, target)
    print(result)
