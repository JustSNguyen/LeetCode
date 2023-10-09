from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def find_index_of_first_element(target: int) -> int:
            left = 0
            right = len(nums) - 1

            while left < right - 1:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            return -1

        def find_last_index_of_element(target: int) -> int:
            left = 0
            right = len(nums) - 1

            while left < right - 1:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            if nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            return -1

        return [find_index_of_first_element(target), find_last_index_of_element(target)]

if __name__ == '__main__':
    nums = [5]
    target = 6
    sol = Solution()
    result = sol.searchRange(nums, target)
    print(result)