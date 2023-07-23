class Solution:
    def isHappy(self, n: int) -> bool:
        saved_numbers = dict()

        def get_square_digits_sum(number):
            total_digits_sum = 0 

            while number > 0: 
                digit = number % 10 
                total_digits_sum += digit * digit 
                number //= 10 
            
            return total_digits_sum
    
        while n != 1:
            if n in saved_numbers:
                return False 
            
            saved_numbers[n] = True 
            total_digits_sum = get_square_digits_sum(n)

            n = total_digits_sum 
        
        return True 
    
if __name__ == "__main__":
    sol = Solution()
    n = 2
    result = sol.isHappy(n)
    print(result)