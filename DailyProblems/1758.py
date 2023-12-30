import math 

class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)
        even_positions = math.ceil(N / 2)
        odd_positions = N - even_positions 

        number_of_ones_in_even_positions = 0 
        number_of_ones_in_odd_positions = 0 

        for i in range(N):
            if i % 2 == 0 and s[i] == "1":
                number_of_ones_in_even_positions += 1 
            if i % 2 == 1 and s[i] == "1":
                number_of_ones_in_odd_positions += 1 
        
        option1 = number_of_ones_in_even_positions + (odd_positions - number_of_ones_in_odd_positions)
        option2 = (even_positions - number_of_ones_in_even_positions) + number_of_ones_in_odd_positions
        return min(option1, option2)