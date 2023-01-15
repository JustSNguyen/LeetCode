from typing import List
from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = deque()
        remember = 0

        for i in range(len(digits) - 1, -1, -1):
            cur_digit = digits[i] 
            new_value = cur_digit + remember
            if i == len(digits) - 1:
                new_value += 1
            if new_value >= 10:
                remember = 1 
                result.appendleft(new_value % 10)
            else: 
                result.appendleft(new_value)
                remember = 0

        if remember == 1:
            result.appendleft(1)
        return list(result)    

if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([8,9,9,9]))