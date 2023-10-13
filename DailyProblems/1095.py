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
        def find_top_of_mountain():
            left = 0
            right = mountain_arr_length
            while right - left > 1:
                mid = (left + right) // 2

                if mid == 0:
                    left = mid + 1
                    continue

                if mid == mountain_arr_length - 1:
                    right = mid
                    continue

                mid_value = mountain_arr.get(mid)
                mid_left_value = mountain_arr.get(mid - 1)
                mid_right_value = mountain_arr.get(mid + 1)

                is_top_of_mountain = mid_value > mid_left_value and mid_value > mid_right_value
                if is_top_of_mountain:
                    return mid

                is_on_the_left = mid_value < mid_right_value
                if is_on_the_left:
                    left = mid + 1
                else:
                    right = mid

            return left

        def binary_search(start, end, is_increasing):
            left = start
            right = end

            while right - left > 1:
                mid = (right + left) // 2
                mid_value = mountain_arr.get(mid)

                if mid_value == target:
                    return mid

                if mid_value < target:
                    if is_increasing:
                        left = mid + 1
                    else:
                        right = mid

                else:
                    if is_increasing:
                        right = mid
                    else:
                        left = mid + 1

            if mountain_arr.get(left) == target:
                return left

            return -1

        top_of_mountain_index = find_top_of_mountain()
        top_of_mountain_value = mountain_arr.get(top_of_mountain_index)
        if top_of_mountain_value == target:
            return top_of_mountain_index

        first_option = binary_search(0, top_of_mountain_index, True)
        if first_option != -1:
            return first_option

        second_option = binary_search(top_of_mountain_index + 1, mountain_arr_length, False)
        return second_option



if __name__ == '__main__':
    sol = Solution()
    array = [1,2,3,5,3]
    mountain_arr = MountainArray(nums = array)
    target = 3
    result = sol.findInMountainArray(target, mountain_arr)
    print(result)


