from typing import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        mapping = dict()

        number_of_characters_before = 0
        for digit in range(2, 10):
            mapping[f'{digit}'] = []
            number_of_options = 3 
            if digit == 7 or digit == 9: 
                number_of_options = 4

            for option in range(number_of_options):
                ascii_value = ord('a') + number_of_characters_before
                mapping[f'{digit}'].append(chr(ascii_value))
                number_of_characters_before += 1

        cur_all_combinations = ['']

        digit_index = 0 
        while digit_index < len(digits):
            cur_digit = digits[digit_index]
            new_all_combinations = []
            for combination in cur_all_combinations:
                for character in mapping[cur_digit]:
                    new_combination = combination + character
                    new_all_combinations.append(new_combination)
            
            cur_all_combinations = new_all_combinations
            digit_index += 1 
        
        return cur_all_combinations

if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    result = sol.letterCombinations(digits)
    print(result)
            

