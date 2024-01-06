from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_strictly_increasing_subsequence = []

        for num in nums:
            if not longest_strictly_increasing_subsequence:
                longest_strictly_increasing_subsequence.append(num)
            else:
                inserted_index = bisect.bisect_left(longest_strictly_increasing_subsequence, num)
                if inserted_index == len(longest_strictly_increasing_subsequence):
                    longest_strictly_increasing_subsequence.append(num)
                else:
                    longest_strictly_increasing_subsequence[inserted_index] = num

        return len(longest_strictly_increasing_subsequence)

if __name__ == '__main__':
    sol = Solution()
    nums = [7, 7, 7, 7, 7, 7]
    result = sol.lengthOfLIS(nums)
    print(result)