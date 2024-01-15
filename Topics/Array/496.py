from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_greater_of = dict()
        decreasing_stack = []

        for i in range(len(nums2)):
            while decreasing_stack and decreasing_stack[-1] < nums2[i]:
                top = decreasing_stack.pop()
                first_greater_of[top] = nums2[i]

            decreasing_stack.append(nums2[i])

        return [first_greater_of[num] if num in first_greater_of else -1 for num in nums1]

if __name__ == '__main__':
    sol = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    result = sol.nextGreaterElement(nums1, nums2)
    print(result)