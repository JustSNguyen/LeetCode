import math 
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n == 1:
            return x 
        
        abs_n = abs(n)
        temp = self.myPow(x, math.floor(abs_n / 2)) * self.myPow(x, math.ceil(abs_n / 2))
        if n < 0:
            return 1 / temp 
        
        return temp 

if __name__ == '__main__':
    sol = Solution()
    x = 0.00001
    n = 2147483647
    result = sol.myPow(x, n)
    print(result)