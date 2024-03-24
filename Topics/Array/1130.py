from typing import List         

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        decreasing_stack = []
        result = 0 

        for num in arr:
            while decreasing_stack and decreasing_stack[-1] < num:
                cur_leaf = decreasing_stack.pop()

                cost = cur_leaf * num 
                if decreasing_stack:
                    cost = min(cost, cur_leaf * decreasing_stack[-1])

                result += cost 

            decreasing_stack.append(num)
        
        while decreasing_stack:
            cur = decreasing_stack.pop()
            if decreasing_stack:
                result += cur * decreasing_stack[-1]
        
        return result 
