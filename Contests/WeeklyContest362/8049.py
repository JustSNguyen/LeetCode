from collections import deque 

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False 

        go_to_row_fx = abs(fy - sy)
        total_time_taken_to_same_row = go_to_row_fx 
        
        if total_time_taken_to_same_row > t:
            return False 
        
        min_x = sx - go_to_row_fx 
        max_x = sx + go_to_row_fx 

        dist = 0 
        if fx < min_x:
            dist = abs(fx - min_x)
        
        if fx > max_x:
            dist = abs(fx - max_x)

        time_left = t - total_time_taken_to_same_row 

        if dist > time_left:
            return False 
        
        return True 

        
if __name__ == '__main__':
    sol = Solution()
    sx = 1
    sy = 2
    fx = 1
    fy = 1 
    t = 2

    result = sol.isReachableAtTime(sx, sy, fx, fy, t)
    print(result)