class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurences = dict()
        for index, char in enumerate(s):
            if not char in occurences:
                occurences[char] = []
            
            occurences[char].append(index)
        
        first_non_repeating_character = -1 
        for char in occurences:
            number_of_occurences = len(occurences[char])
            if number_of_occurences > 1: 
                continue 

            first_occurence = occurences[char][0]
            if first_non_repeating_character == -1 or first_occurence < first_non_repeating_character:
                first_non_repeating_character = first_occurence

        return first_non_repeating_character 