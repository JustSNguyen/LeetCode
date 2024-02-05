from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lf = 0
        rg = len(nums)

        if target < nums[0] or target > nums[-1]:
            return -1

        while rg - lf > 1:
            mid = (rg + lf) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                rg = mid
            else:
                lf = mid + 1

        if nums[lf] == target:
            return lf

        return -1

if __name__ == '__main__':
    sol = Solution()
    test = [-1,0,3,5,9,12]
    result = sol.search(test, 13)
    print(result)