from typing import List
class MountainArray:
   def __init__(self, nums: List[int]):
       self.nums = nums
   def get(self, index: int) -> int:
       return self.nums[index]
   def length(self) -> int:
       return len(self.nums)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountain_arr_length = mountain_arr.length()
        def index_on_the_left_of_mountain(index):
            if index == 0:
                return True

            else:
                return mountain_arr.get(index) > mountain_arr.get(index - 1)

        def index_on_the_right_of_mountain(index):
            if index == mountain_arr_length - 1:
                return True

            else:
                return mountain_arr.get(index) > mountain_arr.get(index + 1)

        left = 0
        right = mountain_arr_length
        while left < right - 1:
            mid = (left + right) // 2
            mid_value = mountain_arr.get(mid)
            print(mid_value)

            if mid_value == target:
                if index_on_the_left_of_mountain(mid):
                    return mid
                else:
                    right = mid

            if mid_value > target:
                if index_on_the_left_of_mountain(mid):
                    right = mid
                else:
                    left = mid + 1

            if mid_value < target:
                if index_on_the_left_of_mountain(mid):
                    left = mid + 1
                else:
                    right = mid

        if mountain_arr.get(left) == target:
            return left

        return -1

if __name__ == '__main__':
    sol = Solution()
    array = [1, 5, 2]
    mountain_arr = MountainArray(nums = array)
    target = 2
    result = sol.findInMountainArray(target, mountain_arr)
    print(result)


