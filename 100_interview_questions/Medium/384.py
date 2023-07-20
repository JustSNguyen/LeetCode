from typing import List 
import random 

class Solution:

    def __init__(self, nums: List[int]):
        self.default_nums = nums[:]
        self.cur_nums = nums[:]
        
    def reset(self) -> List[int]:
        self.cur_nums = self.default_nums[:]
        return self.cur_nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.cur_nums)
        return self.cur_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()