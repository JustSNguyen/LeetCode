class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0: 
            return 0

        character_count = dict()
        for character in s: 
            if character not in character_count:
                character_count[character] = 0 
            
            character_count[character] += 1
        
        qualified = True 
        for character in character_count:
            if character_count[character] < k: 
                max_string_length = 0
                sub_strings_without_character = s.split(character)
                for substring in sub_strings_without_character:
                    max_string_length = max(max_string_length, self.longestSubstring(substring, k))

                return max_string_length
        
        if qualified:
            return len(s)


if __name__ == "__main__":
    s = "bbaaacbd"
    k = 3
    sol = Solution()
    result = sol.longestSubstring(s, k)
    print(result)

 