class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_length = -1 
        char_position = dict()

        for i, char in enumerate(s):
            if char in char_position:
                max_length = max(max_length, i - char_position[char] - 1)
            else:
                char_position[char] = i 
        
        return max_length