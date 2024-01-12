from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        decreasing_stack = []
        indexes = [i % len(nums) for i in range(2 * len(nums))]
        result = [-1 for _ in range(len(nums))]

        for i in indexes:
            while decreasing_stack and nums[i] > nums[decreasing_stack[-1]]:
                j = decreasing_stack.pop()
                result[j] = nums[i]

            decreasing_stack.append(i)

        return result

if __name__ == '__main__':
    nums = [2, 1]
    sol = Solution()
    result = sol.nextGreaterElements(nums)
    print(result)