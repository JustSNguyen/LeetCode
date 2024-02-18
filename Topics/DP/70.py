class Solution:
    def climbStairs(self, n: int) -> int:
        dp = 0 
        dp_1 = 1 
        dp_2 = 1 

        for i in range(n - 2, -1, -1):
            dp = dp_1 + dp_2 
            dp_2 = dp_1 
            dp_1 = dp 
        
        return dp_1