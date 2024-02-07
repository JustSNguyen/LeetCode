class Solution:
    def isHappy(self, n: int) -> bool:
        existed = set()
        while n != 1:
            existed.add(n)
            new_n = 0 
            while n > 0:
                digit = n % 10 
                new_n += digit * digit 
                n //= 10 
            
            if new_n in existed:
                return False 
            
            n = new_n 
        
        return True 