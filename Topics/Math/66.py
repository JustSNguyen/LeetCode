from typing import List 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            new_digit = digits[i] + carry 
            if new_digit >= 10:
                digits[i] = new_digit % 10 
                carry = 1 
            else:
                digits[i] = new_digit 
                carry = 0 
            
            if carry == 0:
                break 
        
        if carry == 1:
            digits.insert(0, 1)
        
        return digits 