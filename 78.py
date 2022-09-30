from typing import List

class Solution:
    def subsetsHelper(self, cur_index: int, nums: List[int], subset: List[int], subsets: List[List[int]]):
        if cur_index == len(nums):
            subsets.append(subset)
            return 
        
        self.subsetsHelper(cur_index + 1, nums, list(subset), subsets)

        subset.append(nums[cur_index])
        self.subsetsHelper(cur_index + 1, nums, subset, subsets)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subsetsHelper(0, nums, [], result)
        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    sol.subsets(nums)