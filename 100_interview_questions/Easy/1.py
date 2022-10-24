from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = dict()
        for i, num in enumerate(nums): 
            if not num in position:
                position[num] = []

            position[num].append(i)

        for num in position:
            other_num = target - num 
            if other_num != num and other_num in position:
                return [position[num][0], position[other_num][0]]
            
            elif other_num == num and len(position[num]) >= 2:
                return [position[num][0], position[num][1]]

if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))
        