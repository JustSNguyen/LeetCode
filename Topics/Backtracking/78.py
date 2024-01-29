from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def generate(cur_set, index):
            if index == len(nums):
                result.append(cur_set)
                return

            new_set_1 = cur_set[:]
            new_set_1.append(nums[index])
            generate(new_set_1, index + 1)

            new_set_2 = cur_set[:]
            generate(new_set_2, index + 1)

        generate([], 0)

        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    result = sol.subsets(nums)
    print(result)