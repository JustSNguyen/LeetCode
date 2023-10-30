from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_number_of_one_bits(num: int) -> int:
            number_of_one_bits = 0 
            while num > 0:
                bit = num % 2 
                number_of_one_bits += bit 
                num //= 2 
            
            return number_of_one_bits
        
        return sorted(arr, key=lambda num: (get_number_of_one_bits(num), num))