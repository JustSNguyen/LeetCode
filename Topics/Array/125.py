class Solution:
    def isPalindrome(self, s: str) -> bool:
        real_s = []
        for char in s:
            lowercase_char = char.lower()
            if "a" <= lowercase_char <= "z" or "0" <= lowercase_char <= "9":
                real_s.append(lowercase_char)
        
        real_s = "".join(real_s)
        return real_s == real_s[::-1]