class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        result_upper_bound = x + 1

        while result_upper_bound - result > 1:
            mid = (result_upper_bound + result) // 2 
            squared_mid = mid * mid 
            if squared_mid == x:
                return mid 

            if squared_mid > x: 
                result_upper_bound = mid 
            
            else:
                result = mid 
        
        return result 
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.mySqrt(1)
    print(result)
        