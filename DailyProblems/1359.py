from functools import lru_cache

class Solution:
    def countOrders(self, n: int) -> int:
        MODULO = 10 ** 9 + 7 
        max_range = 2 * n 
        
        factorial = [1 for _ in range(max_range + 1)]
        for i in range(2, max_range + 1):
            factorial[i] = ( i * factorial[i - 1] ) % MODULO

        @lru_cache(maxsize = 10**7)
        def C(n, k):
            if k == 0 or k == n: 
                return 1 
            
            return (C(n - 1, k - 1) + C(n - 1, k)) % MODULO 

        result = 1
        for number_of_choices in range(2, max_range + 1, 2):
            result *= C(number_of_choices, 2)
            result %= MODULO 
        
        return result 
    
if __name__ == '__main__':
    sol = Solution()
    n = 500
    print(sol.countOrders(n))
