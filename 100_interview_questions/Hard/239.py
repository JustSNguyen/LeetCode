from typing import List 
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count_num = dict()

        result = []

        for i in range(0, k - 1):
            num = nums[i]
            heapq.heappush(max_heap, -num) 

            if num not in count_num:
                count_num[num] = 0

            count_num[num] += 1
        
        left_pointer = 0
        right_pointer = k - 1

        while right_pointer < len(nums):
            num = nums[right_pointer]

            if num not in count_num:
                count_num[num] = 0 

            count_num[num] += 1 

            heapq.heappush(max_heap, -num)
            
            current_max_num = -max_heap[0]
            while count_num[current_max_num] == 0:
                heapq.heappop(max_heap)
                current_max_num = -max_heap[0]
            
            result.append(current_max_num)

            left_pointer_num = nums[left_pointer]
            count_num[left_pointer_num] -= 1 

            left_pointer += 1 
            right_pointer += 1
        
        return result 

if __name__ == "__main__":
    nums = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    sol = Solution()
    result = sol.maxSlidingWindow(nums, k)
    print(result)
            

