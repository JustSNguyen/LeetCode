from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lf = 0
        rg = len(nums) - 1
        while lf < rg:
            mid = (lf + rg) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[0] > nums[mid]:
                    rg = mid - 1
                else:
                    if target >= nums[0]:
                        rg = mid - 1
                    else:
                        lf = mid + 1

            else:
                if nums[0] <= nums[mid]:
                    lf = mid + 1
                else:
                    if nums[-1] >= target:
                        lf = mid + 1
                    else:
                        rg = mid - 1

        if nums[lf] == target:
            return lf

        return -1

if __name__ == '__main__':
    sol = Solution()
    target = 3
    nums = [5, 1, 3]
    result = sol.search(nums, target)
    print(result)