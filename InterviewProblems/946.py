from typing import List 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0 
        j = 0 
        stack = []
        N = len(pushed)

        while i < N and j < N:
            while not stack or stack[-1] != popped[j]:
                if i == N: return False 
                stack.append(pushed[i])
                i += 1 
            
            j += 1 
            stack.pop()
        
        return True 